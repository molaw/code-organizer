"""
File system utility functions.
"""

import os
from pathlib import Path
from datetime import datetime
from typing import Tuple, List


def get_dir_size(path: Path) -> int:
    """
    Calculate the total size of a directory in bytes.

    Args:
        path: Path to directory

    Returns:
        Total size in bytes
    """
    total_size = 0
    try:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                try:
                    filepath = os.path.join(dirpath, filename)
                    if os.path.exists(filepath) and not os.path.islink(filepath):
                        total_size += os.path.getsize(filepath)
                except (OSError, PermissionError):
                    continue
    except (OSError, PermissionError):
        pass
    return total_size


def format_size(size_bytes: int) -> str:
    """
    Format byte size to human-readable string.

    Args:
        size_bytes: Size in bytes

    Returns:
        Formatted string (e.g., "1.5 GB", "234 MB")
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} PB"


def get_last_modified(path: Path) -> datetime:
    """
    Get the last modified time of a file or directory.

    For directories, finds the most recently modified file.

    Args:
        path: Path to file or directory

    Returns:
        Last modified datetime
    """
    if path.is_file():
        return datetime.fromtimestamp(path.stat().st_mtime)

    # For directories, find the most recently modified file
    latest_time = path.stat().st_mtime
    try:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                try:
                    filepath = os.path.join(dirpath, filename)
                    mtime = os.path.getmtime(filepath)
                    if mtime > latest_time:
                        latest_time = mtime
                except (OSError, PermissionError):
                    continue
    except (OSError, PermissionError):
        pass

    return datetime.fromtimestamp(latest_time)


def count_files(path: Path, extensions: List[str] = None) -> int:
    """
    Count files in a directory, optionally filtering by extension.

    Args:
        path: Path to directory
        extensions: List of extensions to count (e.g., ['.py', '.js'])

    Returns:
        Number of files
    """
    count = 0
    try:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                if extensions is None:
                    count += 1
                elif any(filename.endswith(ext) for ext in extensions):
                    count += 1
    except (OSError, PermissionError):
        pass
    return count


def is_empty_dir(path: Path) -> bool:
    """
    Check if a directory is empty (no files, only empty subdirs allowed).

    Args:
        path: Path to directory

    Returns:
        True if directory is empty
    """
    try:
        for dirpath, dirnames, filenames in os.walk(path):
            if filenames:
                return False
        return True
    except (OSError, PermissionError):
        return False


def should_exclude(path: Path, exclude_patterns: List[str]) -> bool:
    """
    Check if a path should be excluded based on patterns.

    Args:
        path: Path to check
        exclude_patterns: List of patterns to exclude

    Returns:
        True if path should be excluded
    """
    path_str = str(path)
    for pattern in exclude_patterns:
        if pattern in path_str:
            return True
    return False
