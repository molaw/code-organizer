"""
Display utilities for scan results using Rich library.
"""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.tree import Tree
from typing import List

from .quick_scanner import QuickScanResult
from ..utils.file_utils import format_size


console = Console()


def display_quick_scan_results(result: QuickScanResult) -> None:
    """
    Display quick scan results in a beautiful format.

    Args:
        result: QuickScanResult to display
    """
    console.print()
    console.print("=" * 80)
    console.print()

    # Executive Summary
    _display_executive_summary(result)

    console.print()

    # Projects by Type
    _display_projects_by_type(result)

    console.print()

    # Quick Wins
    _display_quick_wins(result)

    console.print()

    # Security Issues
    _display_security_issues(result)

    console.print()

    # Duplicates
    _display_duplicates(result)

    console.print()

    # Empty Folders
    _display_empty_folders(result)

    console.print()
    console.print("=" * 80)
    console.print()


def _display_executive_summary(result: QuickScanResult) -> None:
    """Display executive summary panel."""
    quick_win_size = sum(qw.size for qw in result.quick_wins)

    summary_text = f"""
[bold cyan]QUICK SCAN SUMMARY[/bold cyan]

[green]+[/green] Total Projects Found: [bold]{result.total_projects}[/bold]
[green]+[/green] Total Size: [bold]{format_size(result.total_size)}[/bold]
[yellow]![/yellow] Quick Win Space: [bold]{format_size(quick_win_size)}[/bold] (can be freed safely)
[red]![/red]  Security Issues: [bold]{len(result.security_issues)}[/bold] (need attention)
[blue]*[/blue] Empty Folders: [bold]{len(result.empty_folders)}[/bold]
[magenta]~[/magenta] Potential Duplicates: [bold]{len(result.obvious_duplicates)}[/bold] pairs
    """

    panel = Panel(
        summary_text.strip(),
        title="[bold white]>> QUICK SCAN COMPLETE <<[/bold white]",
        border_style="cyan",
        padding=(1, 2)
    )
    console.print(panel)


def _display_projects_by_type(result: QuickScanResult) -> None:
    """Display projects grouped by type."""
    if not result.projects_by_type:
        return

    table = Table(title="[Projects by Type]", show_header=True, header_style="bold magenta")
    table.add_column("Project Type", style="cyan", width=20)
    table.add_column("Count", justify="right", style="green")
    table.add_column("Percentage", justify="right", style="yellow")

    # Sort by count (descending)
    sorted_types = sorted(
        result.projects_by_type.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for project_type, count in sorted_types:
        percentage = (count / result.total_projects * 100) if result.total_projects > 0 else 0
        table.add_row(
            project_type,
            str(count),
            f"{percentage:.1f}%"
        )

    # Add total row
    table.add_section()
    table.add_row(
        "[bold]TOTAL[/bold]",
        f"[bold]{result.total_projects}[/bold]",
        "[bold]100.0%[/bold]"
    )

    console.print(table)


def _display_quick_wins(result: QuickScanResult) -> None:
    """Display quick win opportunities."""
    if not result.quick_wins:
        console.print(Panel(
            "[green]No quick wins found - your codebase is already clean![/green]",
            title="[Quick Wins]",
            border_style="green"
        ))
        return

    # Group by category
    by_category = {}
    for qw in result.quick_wins:
        if qw.category not in by_category:
            by_category[qw.category] = []
        by_category[qw.category].append(qw)

    table = Table(
        title="[Quick Wins - Safe to Remove]",
        show_header=True,
        header_style="bold yellow"
    )
    table.add_column("Category", style="yellow", width=20)
    table.add_column("Count", justify="right", style="cyan")
    table.add_column("Total Size", justify="right", style="green")

    total_size = 0
    for category, items in sorted(by_category.items()):
        category_size = sum(item.size for item in items)
        total_size += category_size
        table.add_row(
            category,
            str(len(items)),
            format_size(category_size)
        )

    table.add_section()
    table.add_row(
        "[bold]TOTAL POTENTIAL SAVINGS[/bold]",
        f"[bold]{len(result.quick_wins)}[/bold]",
        f"[bold]{format_size(total_size)}[/bold]"
    )

    console.print(table)

    # Show top 5 largest
    if len(result.quick_wins) > 5:
        console.print("\n[dim]Top 5 largest items:[/dim]")
        sorted_wins = sorted(result.quick_wins, key=lambda x: x.size, reverse=True)[:5]
        for i, qw in enumerate(sorted_wins, 1):
            console.print(f"  {i}. {qw.path} ({format_size(qw.size)})")


def _display_security_issues(result: QuickScanResult) -> None:
    """Display security issues."""
    if not result.security_issues:
        console.print(Panel(
            "[green]No obvious security issues detected![/green]",
            title="[Security]",
            border_style="green"
        ))
        return

    table = Table(
        title="[Security Issues - Needs Review]",
        show_header=True,
        header_style="bold red"
    )
    table.add_column("Path", style="yellow", width=60)
    table.add_column("Issue", style="red", width=30)

    # Show up to 10 items
    for path, issue in result.security_issues[:10]:
        table.add_row(str(path), issue)

    if len(result.security_issues) > 10:
        table.add_row(
            f"[dim]... and {len(result.security_issues) - 10} more[/dim]",
            ""
        )

    console.print(table)


def _display_duplicates(result: QuickScanResult) -> None:
    """Display potential duplicates."""
    if not result.obvious_duplicates:
        console.print(Panel(
            "[green]No obvious duplicates detected![/green]",
            title="[Duplicates]",
            border_style="green"
        ))
        return

    console.print(f"\n[bold yellow]Potential Duplicates:[/bold yellow] {len(result.obvious_duplicates)} pairs found")
    console.print("[dim](These need manual review in deep scan)[/dim]\n")

    # Show first 5 pairs
    for i, (path1, path2) in enumerate(result.obvious_duplicates[:5], 1):
        console.print(f"  [cyan]{i}.[/cyan] {path1.name}")
        console.print(f"     ↔  {path2.name}")
        console.print()

    if len(result.obvious_duplicates) > 5:
        console.print(f"  [dim]... and {len(result.obvious_duplicates) - 5} more pairs[/dim]")


def _display_empty_folders(result: QuickScanResult) -> None:
    """Display empty folders."""
    if not result.empty_folders:
        return

    console.print(f"\n[bold blue]Empty Folders:[/bold blue] {len(result.empty_folders)} found")

    if len(result.empty_folders) <= 10:
        for folder in result.empty_folders:
            console.print(f"  • {folder}")
    else:
        for folder in result.empty_folders[:10]:
            console.print(f"  • {folder}")
        console.print(f"  [dim]... and {len(result.empty_folders) - 10} more[/dim]")
