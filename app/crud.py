from .database import load_shoots, save_shoots
from .ui import console, display_shoots, success, error, info

SHOOT_TYPES = [
    "Wedding",
    "Portrait",
    "Product",
    "Event",
    "Fashion",
    "Birthday",
    "Other",
]

PAYMENT_STATUSES = [
    "Pending",
    "Partial",
    "Paid",
]

SHOOT_STATUSES = [
    "Booked",
    "Upcoming",
    "Completed",
    "Editing",
    "Delivered",
    "Cancelled",
]

def get_shoot_by_id(shoots, shoot_id):
    for shoot in shoots:
        if shoot["shoot_id"].lower() == shoot_id.lower():
            return shoot

    return None


def select_from_list(title, options):
    console.print(f"\n[bold cyan]{title}[/bold cyan]")

    for index, option in enumerate(options, start=1):
        console.print(f"[yellow]{index}.[/yellow] {option}")

    while True:
        choice = input("Enter your choice: ").strip()

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(options):
                return options[choice - 1]

        error(f"Please enter a number between 1 and {len(options)}.")


def add_shoot():
    console.print("\n[bold magenta] ADD NEW PHOTOGRAPHY SHOOT[/bold magenta]\n")

    shoots = load_shoots()

    # Shoot ID
    while True:
        shoot_id = input("Enter Shoot ID (example PS001): ").strip()

        if not shoot_id:
            error("Shoot ID cannot be empty.")
            continue

        if get_shoot_by_id(shoots, shoot_id):
            error("This Shoot ID already exists.")
            continue

        break

    client_name = input("Enter client name: ").strip()
    contact = input("Enter contact number: ").strip()

    shoot_type = select_from_list(
        "Select Shoot Type:",
        SHOOT_TYPES
    )
    
    shoot_date = input("Enter shoot date (DD-MM-YYYY): ").strip()
    location = input("Enter shoot location: ").strip()
    photographer = input("Enter photographer name: ").strip()



    while True:
        try:
            budget = float(input("Enter total budget: ₹"))

            if budget < 0:
                error("Budget cannot be negative.")
                continue

            break

        except ValueError:
            error("Please enter a valid amount.")

    while True:
        try:
            amount_paid = float(input("Enter amount paid: ₹"))

            if amount_paid < 0:
                error("Amount paid cannot be negative.")
                continue

            if amount_paid > budget:
                error("Amount paid cannot be greater than the total budget.")
                continue

            break

        except ValueError:
            error("Please enter a valid amount.")

    pending_amount = budget - amount_paid

    if amount_paid == 0:
        payment_status = "Pending"
    elif amount_paid < budget:
        payment_status = "Partial"
    else:
        payment_status = "Paid"

    shoot_status = select_from_list(
        "Select Shoot Status:",
        SHOOT_STATUSES
    )

    delivery_date = input(
        "Enter delivery date (DD-MM-YYYY): "
    ).strip()

    notes = input("Enter notes: ").strip()


    shoot = {
        "shoot_id": shoot_id,
        "client_name": client_name,
        "contact": contact,
        "shoot_type": shoot_type,
        "shoot_date": shoot_date,
        "location": location,
        "photographer": photographer,
        "budget": budget,
        "amount_paid": amount_paid,
        "pending_amount": pending_amount,
        "payment_status": payment_status,
        "shoot_status": shoot_status,
        "delivery_date": delivery_date,
        "notes": notes,
    }

    shoots.append(shoot)
    save_shoots(shoots)

    success("New shoot added successfully!")

    console.print(
        f"\n[bold cyan]Payment Summary[/bold cyan]\n"
        f"Total Budget : ₹{budget:.2f}\n"
        f"Amount Paid  : ₹{amount_paid:.2f}\n"
        f"Pending      : ₹{pending_amount:.2f}\n"
        f"Status       : {payment_status}"
    )



def view_shoots():
    shoots = load_shoots()

    console.print("\n[bold magenta] ALL PHOTOGRAPHY SHOOTS[/bold magenta]\n")

    display_shoots(shoots)



def search_shoot():
    shoots = load_shoots()

    if not shoots:
        info("No shoot records available.")
        return

    console.print("\n[bold magenta]🔍 SEARCH SHOOT[/bold magenta]\n")

    console.print("[cyan]1.[/cyan] Search by Shoot ID")
    console.print("[cyan]2.[/cyan] Search by Client Name")
    console.print("[cyan]3.[/cyan] Search by Shoot Type")
    console.print("[cyan]4.[/cyan] Search by Shoot Status")

    choice = input("\nEnter your choice: ").strip()

    results = []

    if choice == "1":
        shoot_id = input("Enter Shoot ID: ").strip()

        shoot = get_shoot_by_id(shoots, shoot_id)

        if shoot:
            results.append(shoot)

    elif choice == "2":
        client_name = input("Enter client name: ").strip().lower()

        results = [
            shoot
            for shoot in shoots
            if client_name in shoot["client_name"].lower()
        ]

    elif choice == "3":
        shoot_type = select_from_list(
            "Select Shoot Type:",
            SHOOT_TYPES
        )

        results = [
            shoot
            for shoot in shoots
            if shoot["shoot_type"] == shoot_type
        ]

    elif choice == "4":
        shoot_status = select_from_list(
            "Select Shoot Status:",
            SHOOT_STATUSES
        )

        results = [
            shoot
            for shoot in shoots
            if shoot["shoot_status"] == shoot_status
        ]

    else:
        error("Invalid choice.")
        return

    if results:
        display_shoots(results)
    else:
        info("No matching shoot found.")



def update_shoot():
    shoots = load_shoots()

    if not shoots:
        info("No shoot records available.")
        return

    console.print("\n[bold magenta]✏️ UPDATE SHOOT[/bold magenta]\n")

    shoot_id = input("Enter Shoot ID to update: ").strip()

    shoot = get_shoot_by_id(shoots, shoot_id)

    if not shoot:
        error("Shoot not found.")
        return

    console.print(
        f"\n[bold green]Shoot found:[/bold green] "
        f"{shoot['client_name']} - {shoot['shoot_type']}"
    )

    console.print("\n[cyan]What would you like to update?[/cyan]")

    console.print("[yellow]1.[/yellow] Client Name")
    console.print("[yellow]2.[/yellow] Contact")
    console.print("[yellow]3.[/yellow] Shoot Type")
    console.print("[yellow]4.[/yellow] Shoot Date")
    console.print("[yellow]5.[/yellow] Location")
    console.print("[yellow]6.[/yellow] Photographer")
    console.print("[yellow]7.[/yellow] Payment Details")
    console.print("[yellow]8.[/yellow] Shoot Status")
    console.print("[yellow]9.[/yellow] Delivery Date")
    console.print("[yellow]10.[/yellow] Notes")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        shoot["client_name"] = input(
            "Enter new client name: "
        ).strip()

    elif choice == "2":
        shoot["contact"] = input(
            "Enter new contact number: "
        ).strip()

    elif choice == "3":
        shoot["shoot_type"] = select_from_list(
            "Select New Shoot Type:",
            SHOOT_TYPES
        )

    elif choice == "4":
        shoot["shoot_date"] = input(
            "Enter new shoot date (DD-MM-YYYY): "
        ).strip()

    elif choice == "5":
        shoot["location"] = input(
            "Enter new location: "
        ).strip()

    elif choice == "6":
        shoot["photographer"] = input(
            "Enter new photographer name: "
        ).strip()


    elif choice == "7":

        while True:
            try:
                new_budget = float(
                    input(
                        f"Enter total budget "
                        f"(current ₹{shoot['budget']:.2f}): ₹"
                    )
                )

                if new_budget < 0:
                    error("Budget cannot be negative.")
                    continue

                break

            except ValueError:
                error("Please enter a valid amount.")

        while True:
            try:
                new_amount_paid = float(
                    input(
                        f"Enter amount paid "
                        f"(current ₹{shoot['amount_paid']:.2f}): ₹"
                    )
                )

                if new_amount_paid < 0:
                    error("Amount paid cannot be negative.")
                    continue

                if new_amount_paid > new_budget:
                    error(
                        "Amount paid cannot be greater "
                        "than the total budget."
                    )
                    continue

                break

            except ValueError:
                error("Please enter a valid amount.")

        new_pending_amount = new_budget - new_amount_paid

        if new_amount_paid == 0:
            new_payment_status = "Pending"
        elif new_amount_paid < new_budget:
            new_payment_status = "Partial"
        else:
            new_payment_status = "Paid"

        shoot["budget"] = new_budget
        shoot["amount_paid"] = new_amount_paid
        shoot["pending_amount"] = new_pending_amount
        shoot["payment_status"] = new_payment_status

        console.print(
            f"\n[bold cyan]Updated Payment Summary[/bold cyan]\n"
            f"Total Budget : ₹{new_budget:.2f}\n"
            f"Amount Paid  : ₹{new_amount_paid:.2f}\n"
            f"Pending      : ₹{new_pending_amount:.2f}\n"
            f"Status       : {new_payment_status}"
        )

    elif choice == "8":
        shoot["shoot_status"] = select_from_list(
            "Select New Shoot Status:",
            SHOOT_STATUSES
        )

    elif choice == "9":
        shoot["delivery_date"] = input(
            "Enter new delivery date (DD-MM-YYYY): "
        ).strip()

    elif choice == "10":
        shoot["notes"] = input(
            "Enter new notes: "
        ).strip()

    else:
        error("Invalid choice.")
        return

    save_shoots(shoots)

    success("Shoot updated successfully!")



def delete_shoot():
    shoots = load_shoots()

    if not shoots:
        info("No shoot records available.")
        return

    console.print("\n[bold magenta]🗑️ DELETE SHOOT[/bold magenta]\n")

    shoot_id = input("Enter Shoot ID to delete: ").strip()

    shoot = get_shoot_by_id(shoots, shoot_id)

    if not shoot:
        error("Shoot not found.")
        return

    console.print(
        f"\n[bold yellow]Shoot:[/bold yellow] "
        f"{shoot['client_name']} - {shoot['shoot_type']}"
    )

    confirmation = input(
        "\nAre you sure you want to delete this shoot? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":
        shoots.remove(shoot)
        save_shoots(shoots)

        success("Shoot deleted successfully.")

    else:
        info("Delete operation cancelled.")


def show_dashboard():
    shoots = load_shoots()

    if not shoots:
        info("No shoot records available.")
        return

    console.print(
        "\n[bold magenta] PHOTOGRAPHY SHOOT DASHBOARD[/bold magenta]\n"
    )

    total_shoots = len(shoots)

    completed = sum(
        1 for shoot in shoots
        if shoot["shoot_status"] == "Completed"
    )

    upcoming = sum(
        1 for shoot in shoots
        if shoot["shoot_status"] == "Upcoming"
    )

    editing = sum(
        1 for shoot in shoots
        if shoot["shoot_status"] == "Editing"
    )

    delivered = sum(
        1 for shoot in shoots
        if shoot["shoot_status"] == "Delivered"
    )

    cancelled = sum(
        1 for shoot in shoots
        if shoot["shoot_status"] == "Cancelled"
    )

    total_budget = sum(
        float(shoot.get("budget", 0))
        for shoot in shoots
    )

    total_paid = sum(
        float(shoot.get("amount_paid", 0))
        for shoot in shoots
    )

    total_pending = sum(
        float(shoot.get("pending_amount", 0))
        for shoot in shoots
    )

    pending_payments = sum(
        1 for shoot in shoots
        if shoot["payment_status"] == "Pending"
    )

    partial_payments = sum(
        1 for shoot in shoots
        if shoot["payment_status"] == "Partial"
    )

    paid_payments = sum(
        1 for shoot in shoots
        if shoot["payment_status"] == "Paid"
    )

    console.print(
        f"[bold cyan]Total Shoots:[/bold cyan] {total_shoots}"
    )

    console.print(
        f"[bold green]Completed:[/bold green] {completed}"
    )

    console.print(
        f"[bold yellow]Upcoming:[/bold yellow] {upcoming}"
    )

    console.print(
        f"[bold blue]Editing:[/bold blue] {editing}"
    )

    console.print(
        f"[bold green]Delivered:[/bold green] {delivered}"
    )

    console.print(
        f"[bold red]Cancelled:[/bold red] {cancelled}"
    )

    console.print("\n[bold magenta]💰 PAYMENT SUMMARY[/bold magenta]")

    console.print(
        f"Total Budget    : ₹{total_budget:.2f}"
    )

    console.print(
        f"Total Paid      : ₹{total_paid:.2f}"
    )

    console.print(
        f"Total Pending   : ₹{total_pending:.2f}"
    )

    console.print(
        f"\nPending Payments : {pending_payments}"
    )

    console.print(
        f"Partial Payments : {partial_payments}"
    )

    console.print(
        f"Paid Payments    : {paid_payments}"
    )