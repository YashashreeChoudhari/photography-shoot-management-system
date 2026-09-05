from .crud import (
    add_shoot,
    view_shoots,
    search_shoot,
    update_shoot,
    delete_shoot,
    show_dashboard,
)

from .database import load_shoots

from .excel_export import export_to_excel

from .ui import (
    console,
    show_title,
    show_menu,
    success,
    error,
    info,
    pause,
)


def main():
    while True:

        console.clear()

        show_title()
        show_menu()

        choice = input("\nEnter your choice [1-8]: ").strip()

        if choice == "1":
            add_shoot()

        elif choice == "2":
            view_shoots()

        elif choice == "3":
            search_shoot()

        elif choice == "4":
            update_shoot()

        elif choice == "5":
            delete_shoot()

        elif choice == "6":
            show_dashboard()

        elif choice == "7":
            shoots = load_shoots()

            if export_to_excel(shoots):
                success(
                    "Data exported successfully to "
                    "exports/photography_shoots.xlsx"
                )
            else:
                info("No shoot records available for export.")

        elif choice == "8":
            console.print(
                "\n[bold magenta]"
                " Thank you for using Photography Shoot MS!"
                "[/bold magenta]"
            )
            console.print("Goodbye!\n")
            break

        else:
            error("Invalid choice. Please select 1-8.")

        pause()


if __name__ == "__main__":
    main()