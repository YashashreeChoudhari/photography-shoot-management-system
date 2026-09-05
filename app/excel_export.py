from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
from pathlib import Path

EXPORT_FILE = (Path(__file__).parent.parent/ "exports"/ "photography_shoots.xlsx")

def export_to_excel(shoots):
    """Export shoot records to Excel."""

    if not shoots:
        return False

    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Photography Shoots"

    headers = [
        "Shoot ID",
        "Client Name",
        "Contact",
        "Shoot Type",
        "Shoot Date",
        "Location",
        "Photographer",
        "Budget",
        "Amount Paid",
        "Pending Amount",
        "Payment Status",
        "Shoot Status",
        "Delivery Date",
        "Notes",
    ]

    worksheet.append(headers)

    for cell in worksheet[1]:
        cell.font = Font(bold=True)
        cell.alignment = Alignment(horizontal="center")

    for shoot in shoots:
        worksheet.append([
            shoot["shoot_id"],
            shoot["client_name"],
            shoot["contact"],
            shoot["shoot_type"],
            shoot["shoot_date"],
            shoot["location"],
            shoot["photographer"],
            shoot["budget"],
            shoot["amount_paid"],
            shoot["pending_amount"],
            shoot["payment_status"],
            shoot["shoot_status"],
            shoot["delivery_date"],
            shoot["notes"],
        ])

    for column in worksheet.columns:
        max_length = 0
        column_letter = column[0].column_letter

        for cell in column:
            if cell.value:
                max_length = max(
                    max_length,
                    len(str(cell.value))
                )

        worksheet.column_dimensions[
            column_letter
        ].width = min(max_length + 2, 30)

    EXPORT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    workbook.save(EXPORT_FILE)

    return True