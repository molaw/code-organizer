"""
Phase 1A: Quick Scanner

Fast overview scan (5-10 minutes) to provide immediate insights:
- Count projects by type
- Identify obvious duplicates
- Find quick wins (empty folders, build artifacts)
- Security red flags
- Estimate cleanup potential
"""

import os
from pathlib import Path
from typing import Dict, List, Tuple, Set
from dataclasses import dataclass, field
from datetime import datetime, timedelta

from ..utils.file_utils import (
    get_dir_size, format_size, is_empty_dir,
    should_exclude, count_files
)
from ..utils.progress import create_progress
from ..utils.logger import get_logger


@dataclass
class QuickWin:
    """Represents a quick win opportunity."""
    category: str
    path: Path
    size: int
    reason: str


@dataclass
class ProjectSummary:
    """Basic project information from quick scan."""
    path: Path
    project_type: str
    size: int
    last_modified: datetime
    file_count: int
    has_git: bool


@dataclass
class QuickScanResult:
    """Results from quick scan."""
    projects_by_type: Dict[str, int] = field(default_factory=dict)
    total_projects: int = 0
    total_size: int = 0
    obvious_duplicates: List[Tuple[Path, Path]] = field(default_factory=list)
    quick_wins: List[QuickWin] = field(default_factory=list)
    security_issues: List[Tuple[Path, str]] = field(default_factory=list)
    empty_folders: List[Path] = field(default_factory=list)
    projects: List[ProjectSummary] = field(default_factory=list)


class QuickScanner:
    """Quick scanner for Phase 1A."""

    # Project type indicators (filename patterns)
    PROJECT_PATTERNS = {
        '.NET': ['.sln', '.csproj', '.vbproj', '.fsproj'],
        'Python': ['setup.py', 'pyproject.toml', 'requirements.txt'],
        'Arduino': ['.ino', 'platformio.ini'],
        'Node.js': ['package.json'],
        'Docker': ['Dockerfile', 'docker-compose.yml'],
        'C/C++': ['CMakeLists.txt', 'Makefile'],
    }

    # Quick win patterns
    BUILD_ARTIFACTS = ['node_modules', 'build', 'dist', 'bin', 'obj',
                       '__pycache__', '.vs', 'target']

    # Security patterns (simple check)
    SECURITY_PATTERNS = [
        'id_rsa', 'id_dsa', '.pem', '.key', 'credentials.json',
        'secrets.json', '.env'
    ]

    def __init__(self, search_paths: List[str], exclude_patterns: List[str]):
        """
        Initialize quick scanner.

        Args:
            search_paths: List of paths to search
            exclude_patterns: Patterns to exclude
        """
        self.search_paths = [Path(p).expanduser() for p in search_paths]
        self.exclude_patterns = exclude_patterns
        self.logger = get_logger()
        self.visited_dirs: Set[Path] = set()

    def scan(self) -> QuickScanResult:
        """
        Perform quick scan.

        Returns:
            QuickScanResult with findings
        """
        result = QuickScanResult()

        self.logger.info("Starting Quick Scan (Phase 1A)...")
        self.logger.info("This will take 5-10 minutes for a fast overview.\n")

        with create_progress() as progress:
            task = progress.add_task(
                "[cyan]Scanning directories...",
                total=len(self.search_paths)
            )

            for search_path in self.search_paths:
                if not search_path.exists():
                    self.logger.warning(f"Path does not exist: {search_path}")
                    progress.advance(task)
                    continue

                self._scan_directory(search_path, result)
                progress.advance(task)

        # Post-process results
        self._find_duplicates(result)
        self._calculate_totals(result)

        return result

    def _scan_directory(
        self,
        directory: Path,
        result: QuickScanResult,
        depth: int = 0
    ) -> None:
        """
        Recursively scan directory.

        Args:
            directory: Directory to scan
            result: Result object to populate
            depth: Current recursion depth
        """
        # Avoid infinite loops with symlinks
        try:
            directory = directory.resolve()
        except (OSError, RuntimeError):
            return

        if directory in self.visited_dirs:
            return
        self.visited_dirs.add(directory)

        # Check exclusions
        if should_exclude(directory, self.exclude_patterns):
            return

        # Limit depth to avoid very deep recursion
        if depth > 10:
            return

        try:
            entries = list(directory.iterdir())
        except (OSError, PermissionError):
            return

        # Check if this is a project directory
        project_type = self._detect_project_type(directory)
        if project_type:
            self._process_project(directory, project_type, result)
            # Don't recurse into project directories to avoid nested projects
            return

        # Check for quick wins
        self._check_quick_wins(directory, result)

        # Check for security issues
        self._check_security(directory, result)

        # Check if empty
        if is_empty_dir(directory):
            result.empty_folders.append(directory)

        # Recurse into subdirectories
        for entry in entries:
            if entry.is_dir():
                self._scan_directory(entry, result, depth + 1)

    def _detect_project_type(self, directory: Path) -> str:
        """
        Detect project type based on indicator files.

        Args:
            directory: Directory to check

        Returns:
            Project type string or empty string if not a project
        """
        try:
            files = {f.name for f in directory.iterdir() if f.is_file()}

            # Check for git repo
            has_git_dir = (directory / '.git').exists()

            # Check each project type
            for project_type, patterns in self.PROJECT_PATTERNS.items():
                for pattern in patterns:
                    if pattern in files:
                        return project_type

            # If has .git but no recognized patterns, it's still a project
            if has_git_dir and len(files) > 0:
                return 'Unknown'

        except (OSError, PermissionError):
            pass

        return ''

    def _process_project(
        self,
        directory: Path,
        project_type: str,
        result: QuickScanResult
    ) -> None:
        """
        Process a discovered project.

        Args:
            directory: Project directory
            project_type: Type of project
            result: Result object to update
        """
        # Count by type
        result.projects_by_type[project_type] = \
            result.projects_by_type.get(project_type, 0) + 1

        # Get basic info
        size = get_dir_size(directory)
        try:
            last_modified = datetime.fromtimestamp(directory.stat().st_mtime)
        except (OSError, PermissionError):
            last_modified = datetime.now()

        file_count = count_files(directory)
        has_git = (directory / '.git').exists()

        # Create summary
        summary = ProjectSummary(
            path=directory,
            project_type=project_type,
            size=size,
            last_modified=last_modified,
            file_count=file_count,
            has_git=has_git
        )
        result.projects.append(summary)

    def _check_quick_wins(self, directory: Path, result: QuickScanResult) -> None:
        """
        Check for quick win opportunities.

        Args:
            directory: Directory to check
            result: Result object to update
        """
        dir_name = directory.name.lower()

        if dir_name in self.BUILD_ARTIFACTS:
            size = get_dir_size(directory)
            if size > 1024 * 1024:  # > 1MB
                quick_win = QuickWin(
                    category="Build Artifacts",
                    path=directory,
                    size=size,
                    reason=f"{dir_name} directory"
                )
                result.quick_wins.append(quick_win)

    def _check_security(self, directory: Path, result: QuickScanResult) -> None:
        """
        Check for obvious security issues.

        Args:
            directory: Directory to check
            result: Result object to update
        """
        try:
            for entry in directory.iterdir():
                if entry.is_file():
                    name = entry.name.lower()
                    for pattern in self.SECURITY_PATTERNS:
                        if pattern in name:
                            result.security_issues.append(
                                (entry, f"Potential sensitive file: {pattern}")
                            )
        except (OSError, PermissionError):
            pass

    def _find_duplicates(self, result: QuickScanResult) -> None:
        """
        Find obvious duplicates based on name patterns.

        Args:
            result: Result object to update
        """
        # Group projects by base name
        name_groups: Dict[str, List[Path]] = {}

        for project in result.projects:
            # Get base name (remove -backup, -old, etc.)
            base_name = project.path.name.lower()
            for suffix in ['-backup', '-old', '-copy', '-final', '-v2', '-temp']:
                base_name = base_name.replace(suffix, '')

            if base_name not in name_groups:
                name_groups[base_name] = []
            name_groups[base_name].append(project.path)

        # Find groups with multiple projects
        for base_name, paths in name_groups.items():
            if len(paths) > 1:
                # Add all combinations as potential duplicates
                for i in range(len(paths)):
                    for j in range(i + 1, len(paths)):
                        result.obvious_duplicates.append((paths[i], paths[j]))

    def _calculate_totals(self, result: QuickScanResult) -> None:
        """
        Calculate total statistics.

        Args:
            result: Result object to update
        """
        result.total_projects = len(result.projects)
        result.total_size = sum(p.size for p in result.projects)
