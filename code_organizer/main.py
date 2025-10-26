"""
Main CLI entry point for Code Organizer.

This module provides the command-line interface for all operations.
"""

import click
from pathlib import Path
from rich.console import Console

from .config import load_config, expand_path, Config
from .phase1_scan.quick_scanner import QuickScanner
from .phase1_scan.display import display_quick_scan_results
from .utils.logger import get_logger


console = Console()


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """
    Code Organizer - Scan, analyze, and organize scattered source code.

    A comprehensive tool to help manage years of accumulated development
    projects across your entire computer.
    """
    pass


@cli.command(name="scan-quick")
@click.option(
    '--config',
    '-c',
    type=click.Path(exists=True),
    help='Path to configuration file'
)
@click.option(
    '--paths',
    '-p',
    multiple=True,
    help='Specific paths to scan (overrides config)'
)
def scan_quick(config: str, paths: tuple):
    """
    Perform a quick scan (Phase 1A) - Fast 5-10 minute overview.

    This scan provides immediate insights:
    - Count projects by type
    - Identify obvious duplicates
    - Find quick wins (build artifacts, empty folders)
    - Detect security red flags
    - Estimate cleanup potential

    Examples:
        code-organizer scan-quick
        code-organizer scan-quick --paths ~/Desktop --paths ~/Documents
        code-organizer scan-quick --config my_config.yaml
    """
    console.print("\n[bold cyan]Code Organizer - Quick Scan[/bold cyan]\n")

    # Load configuration
    config_path = Path(config) if config else None
    cfg = load_config(config_path)

    # Use provided paths or config paths
    if paths:
        search_paths = list(paths)
    else:
        search_paths = cfg.scan.search_paths

    # Initialize logger
    logger = get_logger(log_level=cfg.logging.log_level)
    logger.info(f"Searching in: {', '.join(search_paths)}")

    # Create scanner
    scanner = QuickScanner(
        search_paths=search_paths,
        exclude_patterns=cfg.scan.exclude_paths
    )

    # Perform scan
    try:
        result = scanner.scan()

        # Display results
        display_quick_scan_results(result)

        # Summary message
        console.print(
            "\n[bold green]>> Quick scan complete![/bold green]\n"
        )
        console.print(
            "Next steps:\n"
            "  - Run [cyan]code-organizer scan[/cyan] for a comprehensive deep analysis\n"
            "  - Run [cyan]code-organizer scan-quick --help[/cyan] for more options\n"
        )

        logger.info(f"Scan complete. Log saved to: {logger.get_log_file()}")

    except KeyboardInterrupt:
        console.print("\n\n[yellow]! Scan interrupted by user.[/yellow]")
        logger.warning("Scan interrupted by user")
    except Exception as e:
        console.print(f"\n\n[red]X Error during scan: {e}[/red]")
        logger.error(f"Scan failed: {e}", exc_info=True)
        raise click.Abort()


@cli.command(name="scan")
def scan():
    """
    Perform a comprehensive deep scan (Phase 1B) - 30-60 minutes.

    This provides complete analysis including git operations, security scanning,
    duplicate detection, code mining, and relationship analysis.

    (Not yet implemented - use scan-quick for now)
    """
    console.print("[yellow]Deep scan not yet implemented. Use 'scan-quick' for now.[/yellow]")


@cli.command(name="organize")
def organize():
    """
    Run Phase 2 organization and cleanup operations.

    (Not yet implemented)
    """
    console.print("[yellow]Phase 2 not yet implemented.[/yellow]")


if __name__ == '__main__':
    cli()
