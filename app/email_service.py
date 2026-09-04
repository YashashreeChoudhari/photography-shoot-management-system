import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")


def send_excel_email(receiver_email, file_path):
    try:
        # Create email
        message = EmailMessage()

        message["Subject"] = "Photography Shoot Report"
        message["From"] = EMAIL_ADDRESS
        message["To"] = receiver_email

        message.set_content(
            "Hello,\n\n"
            "Please find the Photography Shoot Report attached.\n\n"
            "Regards,\n"
            "Photography Shoot Management System"
        )

        # Read Excel file
        with open(file_path, "rb") as file:
            file_data = file.read()

        # Attach Excel file
        message.add_attachment(
            file_data,
            maintype="application",
            subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            filename=os.path.basename(file_path)
        )

        # Connect to Gmail
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_APP_PASSWORD)

            # Send email
            server.send_message(message)

        return True

    except Exception as e:
        print("Email sending failed.")
        print("Error:", e)
        return False
    
if __name__ == "__main__":
    receiver = input("Enter receiver email: ").strip()

    success = send_excel_email(
        receiver,
        "exports/photography_shoots.xlsx"
    )

    if success:
        print("✅ Excel report sent successfully!")