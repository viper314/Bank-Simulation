🏦 Banking Simulation System (Python – Tkinter)

A desktop-based Banking Simulation Application developed using Python and Tkinter, designed to replicate core banking operations such as account creation, secure login, balance management, and fund transfers with OTP-based email verification.

📌 Features

🔐 User Authentication

New user registration

Existing user login

Forgot password with OTP verification

👤 Account Management

Create bank account with auto-generated account number

Update personal details (name, email, mobile, password)

View account details (balance, Aadhaar, email, open date)

💰 Banking Operations

Deposit money

Withdraw money with Email OTP verification

Transfer funds between accounts with OTP security

📧 Email Integration

Automatic email for account credentials

OTP sent via email for withdrawals, transfers, and password recovery

🗄️ Database Support

SQLite database for secure and persistent data storage

Automatic table creation at runtime

🖥️ User-Friendly GUI

Built using Tkinter

Fullscreen responsive interface

Real-time date and clock display

🛠️ Technologies Used

Programming Language: Python

GUI Framework: Tkinter

Database: SQLite3

Email Handling: SMTP (custom EmailHandler module)

Image Processing: Pillow (PIL)

Security: OTP-based verification

Regex: Input validation (Email, Mobile, Aadhaar)

📂 Project Structure
📁 Banking-Simulation
│
├── main.py                 # Main application file
├── TableCreator.py         # Database & table creation logic
├── Generator.py            # Password & OTP generation
├── EmailHandler.py         # Email & OTP sending logic
├── mybank.sqlite           # SQLite database (auto-created)
├── bank2.png               # Bank logo image
└── README.md               # Project documentation

▶️ How to Run the Project

Clone the repository

git clone https://github.com/your-username/banking-simulation.git


Install required dependencies

pip install pillow


Run the application

python main.py


⚠️ Make sure email credentials are correctly configured inside EmailHandler.py.

🔐 Security Highlights

OTP verification for:

Withdrawals

Fund transfers

Password recovery

Limited OTP attempts (3 tries)

Input validation using Regular Expressions

🎯 Learning Outcomes

Hands-on experience with Tkinter GUI development

Practical use of SQLite databases

Implementing email-based OTP security

Structuring a real-world Python desktop application

Understanding banking workflows

🚀 Future Enhancements

Transaction history & mini statement

Admin dashboard

Encryption for stored passwords

Multi-language UI support

Dark mode theme
