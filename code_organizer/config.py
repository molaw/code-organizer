"""
Configuration management for the Code Organizer tool.

Loads and validates YAML configuration files.
"""

import yaml
from pathlib import Path
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class ScanConfig:
    """Configuration for scanning operations."""
    search_paths: List[str] = field(default_factory=lambda: [str(Path.home())])
    exclude_paths: List[str] = field(default_factory=lambda: [
        "/node_modules", "/.venv", "/venv", "/env", "/build", "/dist",
        "/bin", "/obj", "/__pycache__", "/.vs", "/target",
        "/Library", "/System", "/Windows", "/Program Files"
    ])
    obsolete_threshold_years: int = 5
    reference_threshold_years: int = 2
    active_threshold_months: int = 6
    minimum_file_count: int = 3


@dataclass
class OrganizationConfig:
    """Configuration for organization strategy."""
    keep_archives_separate: bool = True
    archive_location: str = "~/CodeArchive"
    extract_reusables: bool = True
    reusables_location: str = "~/CodeLibrary"
    organized_location: str = "~/CodeOrganized"
    group_by: str = "technology"  # technology, date, type, client


@dataclass
class CleanupConfig:
    """Configuration for cleanup preferences."""
    aggressive_mode: bool = False
    auto_remove_build_artifacts: bool = True
    auto_remove_empty_folders: bool = True
    auto_remove_node_modules: bool = True
    auto_remove_pycache: bool = True
    auto_remove_vs_folders: bool = True
    auto_remove_old_venvs: bool = True


@dataclass
class DuplicateConfig:
    """Configuration for duplicate detection."""
    similarity_threshold: int = 85
    use_content_hash: bool = True
    use_structure_compare: bool = True
    check_git_remotes: bool = True
    duplicate_name_patterns: List[str] = field(default_factory=lambda: [
        "*-backup", "*-old", "*-copy", "Copy of *", "*-final",
        "*-final-final", "*-v2", "*-temp"
    ])


@dataclass
class SecurityConfig:
    """Configuration for security scanning."""
    scan_for_secrets: bool = True
    scan_git_history: bool = True
    scan_for_iot_credentials: bool = True


@dataclass
class GitConfig:
    """Configuration for git operations."""
    default_visibility: str = "private"
    require_confirmation_for_push: bool = True
    scan_for_secrets_before_push: bool = True


@dataclass
class BackupConfig:
    """Configuration for backup operations."""
    create_backup: bool = True
    backup_location: str = "~/CodeOrganization_Backups"
    include_git_bundles: bool = True
    compress_backup: bool = False


@dataclass
class LoggingConfig:
    """Configuration for logging."""
    log_level: str = "INFO"
    log_location: str = "~/CodeOrganization_Logs"
    create_separate_git_log: bool = True


@dataclass
class Config:
    """Main configuration class."""
    scan: ScanConfig = field(default_factory=ScanConfig)
    organization: OrganizationConfig = field(default_factory=OrganizationConfig)
    cleanup: CleanupConfig = field(default_factory=CleanupConfig)
    duplicate: DuplicateConfig = field(default_factory=DuplicateConfig)
    security: SecurityConfig = field(default_factory=SecurityConfig)
    git: GitConfig = field(default_factory=GitConfig)
    backup: BackupConfig = field(default_factory=BackupConfig)
    logging: LoggingConfig = field(default_factory=LoggingConfig)


def load_config(config_path: Optional[Path] = None) -> Config:
    """
    Load configuration from YAML file or use defaults.

    Args:
        config_path: Path to configuration file (optional)

    Returns:
        Config instance
    """
    if config_path is None or not config_path.exists():
        # Use default configuration
        return Config()

    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)

        if yaml_data is None:
            return Config()

        # Parse configuration sections
        config = Config()

        if 'scan' in yaml_data:
            scan_data = yaml_data['scan']
            config.scan = ScanConfig(
                search_paths=scan_data.get('search_paths', config.scan.search_paths),
                exclude_paths=scan_data.get('exclude_paths', config.scan.exclude_paths),
                obsolete_threshold_years=scan_data.get('obsolete_threshold_years', 5),
                reference_threshold_years=scan_data.get('reference_threshold_years', 2),
                active_threshold_months=scan_data.get('active_threshold_months', 6),
                minimum_file_count=scan_data.get('minimum_file_count', 3)
            )

        if 'organization_strategy' in yaml_data:
            org_data = yaml_data['organization_strategy']
            config.organization = OrganizationConfig(
                keep_archives_separate=org_data.get('keep_archives_separate', True),
                archive_location=org_data.get('archive_location', '~/CodeArchive'),
                extract_reusables=org_data.get('extract_reusables', True),
                reusables_location=org_data.get('reusables_location', '~/CodeLibrary'),
                organized_location=org_data.get('organized_location', '~/CodeOrganized'),
                group_by=org_data.get('group_by', 'technology')
            )

        if 'cleanup_preferences' in yaml_data:
            cleanup_data = yaml_data['cleanup_preferences']
            config.cleanup = CleanupConfig(
                aggressive_mode=cleanup_data.get('aggressive_mode', False),
                auto_remove_build_artifacts=cleanup_data.get('auto_remove_build_artifacts', True),
                auto_remove_empty_folders=cleanup_data.get('auto_remove_empty_folders', True),
                auto_remove_node_modules=cleanup_data.get('auto_remove_node_modules', True),
                auto_remove_pycache=cleanup_data.get('auto_remove_pycache', True),
                auto_remove_vs_folders=cleanup_data.get('auto_remove_vs_folders', True),
                auto_remove_old_venvs=cleanup_data.get('auto_remove_old_venvs', True)
            )

        return config

    except Exception as e:
        print(f"Warning: Error loading config file: {e}")
        print("Using default configuration.")
        return Config()


def expand_path(path_str: str) -> Path:
    """
    Expand user home directory and resolve path.

    Args:
        path_str: Path string (may contain ~)

    Returns:
        Resolved Path object
    """
    return Path(path_str).expanduser().resolve()
