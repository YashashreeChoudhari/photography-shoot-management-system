from rich.console import Console
from rich.panel import Panel
from rich.table import Table


console = Console()


def show_title():
    """Display application title."""

    console.print(
        Panel(
            "[bold magenta] PHOTOGRAPHY SHOOT MANAGEMENT SYSTEM[/bold magenta]\n"
            "[cyan]Manage clients, shoots, payments and delivery status[/cyan]",
            expand=False,
        )
    )


def show_menu():
    """Display the main menu."""

    console.print(
        Panel(
            """
[bold cyan]1.[/bold cyan]  Add New Shoot
[bold cyan]2.[/bold cyan]  View All Shoots
[bold cyan]3.[/bold cyan]  Search Shoot
[bold cyan]4.[/bold cyan]  Update Shoot
[bold cyan]5.[/bold cyan]  Delete Shoot
[bold cyan]6.[/bold cyan]  Dashboard
[bold cyan]7.[/bold cyan]  Export to Excel
[bold cyan]8.[/bold cyan]  Exit
""",
            title="[bold yellow]MAIN MENU[/bold yellow]",
            expand=False,
        )
    )


def display_shoots(shoots):
    """Display shoots in a Rich table."""

    if not shoots:
        console.print("[yellow]No shoot records found.[/yellow]")
        return

    table = Table(title=" Photography Shoots")

    table.add_column("ID", style="cyan")
    table.add_column("Client")
    table.add_column("Type")
    table.add_column("Date")
    table.add_column("Location")
    table.add_column("Photographer")
    table.add_column("Budget")
    table.add_column("Paid")
    table.add_column("Pending")
    table.add_column("Payment")
    table.add_column("Status")

    for shoot in shoots:
        table.add_row(
            shoot["shoot_id"],
            shoot["client_name"],
            shoot["shoot_type"],
            shoot["shoot_date"],
            shoot["location"],
            shoot["photographer"],
            f"₹{shoot['budget']}",
            f"₹{shoot['amount_paid']:.2f}",
            f"₹{shoot['pending_amount']:.2f}",

            shoot["payment_status"],
            shoot["shoot_status"],
        )

    console.print(table)

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# ... your existing functions ...

def success(message):
    console.print(f"[bold green] {message}[/bold green]")

def error(message):
    console.print(f"[bold red] {message}[/bold red]")

def info(message):
    console.print(f"[bold cyan]{message}[/bold cyan]")

def pause():
    while True:
        key = input("\nPress Enter to continue...")

        if key == "":
            break

        print(" Please press only Enter.")