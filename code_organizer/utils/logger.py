"""
Logging utilities for the Code Organizer tool.

Provides structured logging with file output and console output.
"""

import logging
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional


class CodeOrganizerLogger:
    """Logger with file and console output."""

    def __init__(
        self,
        name: str = "code_organizer",
        log_level: str = "INFO",
        log_dir: Optional[Path] = None
    ):
        """
        Initialize the logger.

        Args:
            name: Logger name
            log_level: Logging level (DEBUG, INFO, WARNING, ERROR)
            log_dir: Directory for log files (default: ~/CodeOrganization_Logs)
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(getattr(logging, log_level.upper()))

        # Remove existing handlers
        self.logger.handlers.clear()

        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter('%(message)s')
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)

        # File handler
        if log_dir is None:
            log_dir = Path.home() / "CodeOrganization_Logs"

        log_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        log_file = log_dir / f"code_organizer_{timestamp}.log"

        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)

        self.log_file = log_file

    def debug(self, message: str) -> None:
        """Log debug message."""
        self.logger.debug(message)

    def info(self, message: str) -> None:
        """Log info message."""
        self.logger.info(message)

    def warning(self, message: str) -> None:
        """Log warning message."""
        self.logger.warning(message)

    def error(self, message: str, exc_info: bool = False) -> None:
        """Log error message."""
        self.logger.error(message, exc_info=exc_info)

    def critical(self, message: str) -> None:
        """Log critical message."""
        self.logger.critical(message)

    def get_log_file(self) -> Path:
        """Return the path to the current log file."""
        return self.log_file


# Global logger instance
_logger: Optional[CodeOrganizerLogger] = None


def get_logger(
    name: str = "code_organizer",
    log_level: str = "INFO",
    log_dir: Optional[Path] = None
) -> CodeOrganizerLogger:
    """
    Get or create the global logger instance.

    Args:
        name: Logger name
        log_level: Logging level
        log_dir: Log directory

    Returns:
        CodeOrganizerLogger instance
    """
    global _logger
    if _logger is None:
        _logger = CodeOrganizerLogger(name, log_level, log_dir)
    return _logger
