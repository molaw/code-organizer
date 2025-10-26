"""
Progress tracking utilities using the Rich library.
"""

from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    TaskProgressColumn,
    TimeRemainingColumn,
    TimeElapsedColumn,
)
from rich.console import Console
from typing import Optional


def create_progress() -> Progress:
    """
    Create a Rich progress bar with standard configuration.

    Returns:
        Configured Progress instance
    """
    return Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        TimeElapsedColumn(),
        TimeRemainingColumn(),
        console=Console(),
        transient=False
    )


def create_spinner_progress() -> Progress:
    """
    Create a Rich progress spinner (no bar, for indefinite tasks).

    Returns:
        Configured Progress instance
    """
    return Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        TimeElapsedColumn(),
        console=Console(),
        transient=False
    )
