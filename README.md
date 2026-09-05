# 📸 Photography Shoot Management System

A menu-driven **Python CRUD application** for managing photography shoots, clients, payments, photographers, delivery status, and reports.

The application runs in the terminal and uses the **Rich library** to provide an attractive and user-friendly interface. Shoot records are stored in a JSON file and can be exported to Excel. The project also includes email functionality for sending the generated Excel report.

---

## 📌 Project Overview

Managing photography shoots manually can become difficult when there are multiple clients, photographers, payments, and delivery deadlines.

The **Photography Shoot Management System** provides a simple digital solution to manage all important shoot information from one application.

The system allows the user to:

* Add new photography shoots
* View all shoots
* Search shoots
* Update shoot information
* Delete shoots
* View a dashboard
* Track total budget, paid amount, and pending amount
* Track payment status
* Track shoot status
* Export shoot records to Excel
* Send the Excel report through email

---

## ✨ Features

### 1. Add New Shoot

Users can add a new photography shoot with details such as:

* Shoot ID
* Client name
* Contact number
* Shoot type
* Shoot date
* Location
* Photographer
* Total budget
* Amount paid
* Pending amount
* Payment status
* Shoot status
* Delivery date
* Notes

The system automatically calculates the pending amount:

```text
Pending Amount = Total Budget - Amount Paid
```

The payment status is also calculated automatically:

```text
Amount Paid = 0
→ Pending

Amount Paid < Total Budget
→ Partial

Amount Paid = Total Budget
→ Paid
```

---

### 2. View All Shoots

Displays all saved photography shoots in a formatted Rich table.

The table includes:

* Shoot ID
* Client
* Shoot Type
* Date
* Location
* Photographer
* Budget
* Amount Paid
* Pending Amount
* Payment Status
* Shoot Status

---

### 3. Search Shoot

Users can search for shoots using:

* Shoot ID
* Client Name
* Shoot Type
* Shoot Status

This makes it easier to find a specific shoot from multiple records.

---

### 4. Update Shoot

Existing shoot records can be updated.

The system allows updating:

* Client name
* Contact
* Shoot type
* Shoot date
* Location
* Photographer
* Payment details
* Shoot status
* Delivery date
* Notes

When payment details are updated, the system recalculates:

```text
Pending Amount
Payment Status
```

---

### 5. Delete Shoot

Users can delete a shoot by entering its Shoot ID.

Before deleting the record, the system asks for confirmation to prevent accidental deletion.

---

### 6. Dashboard

The dashboard provides a quick overview of the photography business.

It displays:

* Total shoots
* Completed shoots
* Upcoming shoots
* Editing shoots
* Delivered shoots
* Cancelled shoots
* Total budget
* Total amount paid
* Total pending amount
* Pending payments
* Partial payments
* Paid payments

---

### 7. Excel Export

The application can export all shoot records to an Excel file.

The generated file is:

```text
exports/photography_shoots.xlsx
```

The Excel report contains all major shoot and payment information.

The Excel file is created using the **OpenPyXL** library.

---

### 8. Email Excel Report

The project includes an email service that can send the generated Excel report as an email attachment.

The email functionality uses:

* Python `smtplib`
* `EmailMessage`
* Gmail SMTP
* `python-dotenv`

Email credentials are stored in a `.env` file instead of being hardcoded into the Python source code.

---

## 🛠️ Technologies Used

| Technology        | Purpose                                 |
| ----------------- | --------------------------------------- |
| **Python**        | Main programming language               |
| **Rich**          | Attractive terminal user interface      |
| **JSON**          | Data storage                            |
| **OpenPyXL**      | Excel file generation                   |
| **smtplib**       | Sending emails                          |
| **EmailMessage**  | Creating email messages and attachments |
| **python-dotenv** | Loading environment variables           |
| **Git**           | Version control                         |
| **GitHub**        | Remote code repository                  |

---

## 📂 Project Structure

```text
photography-shoot-management-system/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── crud.py
│   ├── database.py
│   ├── ui.py
│   ├── excel_export.py
│   └── email_service.py
│
├── data/
│   └── shoots.json
│
├── exports/
│   └── .gitkeep
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🧩 Project Architecture

The application is divided into separate modules so that each file has a specific responsibility.

```text
                     main.py
                        │
          ┌─────────────┼─────────────┐
          │             │             │
          ▼             ▼             ▼
       crud.py      database.py   excel_export.py
          │             │             │
          │             ▼             ▼
          │         shoots.json    Excel file
          │
          ▼
        ui.py
          │
          ▼
     Rich Interface

          │
          ▼
   email_service.py
          │
          ▼
    Gmail SMTP Server
```

### Module Responsibilities

#### `main.py`

Controls the main menu and connects all application modules.

#### `crud.py`

Contains the main CRUD operations:

* Create
* Read
* Update
* Delete
* Search
* Dashboard calculations

#### `database.py`

Handles JSON data storage.

It uses:

```python
json.load()
```

to read data and:

```python
json.dump()
```

to save data.

#### `ui.py`

Handles the terminal user interface using Rich.

It contains:

* Panels
* Tables
* Menus
* Success messages
* Error messages
* Information messages
* Pause function

#### `excel_export.py`

Creates and formats the Excel workbook using OpenPyXL.

#### `email_service.py`

Handles sending the generated Excel report through Gmail SMTP.

---

## 💾 Data Storage

The application uses a JSON file for simple file-based data storage.

Location:

```text
data/shoots.json
```

Example structure:

```json
[
    {
        "shoot_id": "PS001",
        "client_name": "Rahul",
        "contact": "9876543210",
        "shoot_type": "Wedding",
        "shoot_date": "15-09-2026",
        "location": "Pune",
        "photographer": "Amit",
        "budget": 50000,
        "amount_paid": 20000,
        "pending_amount": 30000,
        "payment_status": "Partial",
        "shoot_status": "Upcoming",
        "delivery_date": "25-09-2026",
        "notes": "Full-day wedding shoot"
    }
]
```

JSON was selected because it is simple, lightweight, human-readable, and suitable for a small W1-level project.

---

## 📊 Payment Management

The system automatically manages payment calculations.

### Formula

```text
Pending Amount = Budget - Amount Paid
```

### Payment Status

| Condition            | Status  |
| -------------------- | ------- |
| Amount Paid = 0      | Pending |
| Amount Paid < Budget | Partial |
| Amount Paid = Budget | Paid    |

The system also prevents the user from entering an amount paid greater than the total budget.

---

## 📸 Shoot Status

The application supports the following shoot statuses:

```text
Booked
Upcoming
Completed
Editing
Delivered
Cancelled
```

These statuses help track the progress of a photography project.

---

## 📧 Email Configuration

The email service uses environment variables to protect sensitive credentials.

Create a `.env` file in the project root:

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_APP_PASSWORD=your_app_password
```

The `.env` file should **not be committed to GitHub**.

It is included in `.gitignore`.

### Required Gmail Setup

For Gmail SMTP authentication, use a Gmail **App Password** rather than putting your normal Gmail password into the project.

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the project directory

```bash
cd photography-shoot-management-system
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run the application from the project root:

```bash
python -m app.main
```

The main menu will appear in the terminal.

```text
1. Add New Shoot
2. View All Shoots
3. Search Shoot
4. Update Shoot
5. Delete Shoot
6. Dashboard
7. Export to Excel
8. Exit
```

---

## 📤 Excel Export

To export shoot data:

1. Run the application.
2. Select **Export to Excel**.
3. The application loads the shoot records from JSON.
4. OpenPyXL creates an Excel workbook.
5. The records are added to the worksheet.
6. The Excel file is saved in:

```text
exports/photography_shoots.xlsx
```

---

## 📧 Sending the Excel Report

The email service reads the generated Excel file and sends it as an attachment through Gmail SMTP.

The basic flow is:

```text
Shoot Data
    ↓
JSON
    ↓
Load Data
    ↓
Export to Excel
    ↓
photography_shoots.xlsx
    ↓
Email Service
    ↓
Gmail SMTP
    ↓
Receiver
```

---

## 🔐 Security

Sensitive information such as email credentials is stored in `.env`.

The following file should never be uploaded to GitHub:

```text
.env
```

The `.gitignore` file contains:

```text
.env
```

This prevents Git from tracking the environment file.

---

## 🌿 Git and GitHub

Git is used for version control.

Typical workflow:

```bash
git status
git add .
git commit -m "Add Photography Shoot Management System"
git push
```

GitHub is used to host the remote repository and submit the project.

---

## 🧪 Testing

The following functionality should be tested before submission:

### CRUD Testing

* Add a new shoot
* Try adding a duplicate Shoot ID
* View all shoots
* Search by Shoot ID
* Search by Client Name
* Search by Shoot Type
* Search by Shoot Status
* Update shoot details
* Update payment details
* Delete a shoot
* Cancel a delete operation

### Payment Testing

Test:

```text
Budget = ₹50,000
Paid = ₹0
Pending = ₹50,000
Status = Pending
```

```text
Budget = ₹50,000
Paid = ₹20,000
Pending = ₹30,000
Status = Partial
```

```text
Budget = ₹50,000
Paid = ₹50,000
Pending = ₹0
Status = Paid
```

Also test that:

```text
Amount Paid > Budget
```

is rejected.

### Excel Testing

Verify that:

```text
exports/photography_shoots.xlsx
```

is created and contains the correct shoot information.

### Email Testing

Verify that:

* Email credentials are loaded from `.env`
* SMTP connection works
* Excel file is attached
* Email is sent successfully

---

## 🎯 Learning Objectives

This project demonstrates practical knowledge of:

* Python fundamentals
* Variables and data types
* Lists and dictionaries
* Functions
* Loops
* Conditional statements
* Exception handling
* File handling
* JSON
* CRUD operations
* Modular programming
* Python packages
* Rich library
* Excel automation
* Environment variables
* SMTP email
* Git
* GitHub

---

## 🚀 Future Improvements

Possible future features include:

* Automatic date validation
* Contact number validation
* Upcoming shoots view
* Revenue reports
* Detailed shoot view
* Invoice generation
* Multiple photographers
* Better Excel formatting
* Automatic email from the main menu
* Database integration using SQLite or MySQL
* Graphical user interface
* Login and user authentication

---

## 👨‍💻 Author

**Photography Shoot Management System**

Built as a Python fundamentals and CRUD project demonstrating practical software development concepts, file-based storage, reporting, email integration, and Git/GitHub workflow.

---

## 📄 License

This project is created for educational and learning purposes.
