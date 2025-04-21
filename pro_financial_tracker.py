import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from openpyxl import load_workbook
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox


class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Pro Financial Tracker")
        self.root.geometry("800x700")

        # Initialize the style and theme
        self.style = ttk.Style()
        self.style.theme_use("litera")

        # Light/Dark mode toggle state
        self.current_theme = "litera"  # Light mode by default

        ttk.Label(root, text="💼 Enter Monthly Salary", font=("Segoe UI", 14)).pack(pady=10)
        self.salary_entry = ttk.Entry(root, width=30)
        self.salary_entry.pack()

        self.entries = {}
        categories = [
            "rent", "gym", "internet", "electricity", "transportation",
            "food", "phone_recharged", "charity", "personal_care", "other"
        ]

        form_frame = ttk.Frame(root)
        form_frame.pack(pady=10)

        for i, cat in enumerate(categories):
            row = i // 2
            col = i % 2
            label = ttk.Label(form_frame, text=cat.replace("_", " ").title())
            entry = ttk.Entry(form_frame, width=30)
            label.grid(row=row, column=col*2, padx=5, pady=5, sticky="w")
            entry.grid(row=row, column=col*2+1, padx=5, pady=5)
            self.entries[cat] = entry

        ttk.Button(root, text="📊 Calculate & Save Report", bootstyle=SUCCESS, command=self.calculate).pack(pady=10)

        ttk.Label(root, text="📋 Analysis Result", font=("Segoe UI", 12)).pack()
        self.result_text = ttk.Text(root, height=15, width=90)
        self.result_text.pack(pady=5)

        theme_frame = ttk.Frame(root)
        theme_frame.pack(pady=5)
        ttk.Button(theme_frame, text="🌞 Light Mode", command=lambda: self.toggle_theme("litera")).pack(side=LEFT, padx=5)
        ttk.Button(theme_frame, text="🌙 Dark Mode", command=lambda: self.toggle_theme("darkly")).pack(side=LEFT)

        # Add-ons prompt
        self.add_ons_prompt()

    def toggle_theme(self, theme_name):
        """Toggle between light and dark themes"""
        self.style.theme_use(theme_name)
        self.current_theme = theme_name

    def add_ons_prompt(self):
        """Prompt for potential next add-ons."""
        add_ons = """
💡 Next Add-ons?
Would you like me to add:

🔐 Google Drive backup?
🖨 PDF/Printable report?
📆 Monthly tracker with navigation?
"""
        self.result_text.insert("1.0", add_ons)
        self.result_text.insert("end", "\n")

    def calculate(self):
        try:
            salary = float(self.salary_entry.get().strip())
            bills = {}
            for key, entry in self.entries.items():
                value = entry.get().strip()
                if not value:
                    raise ValueError(f"Missing value for {key.replace('_', ' ').title()}")
                bills[key] = float(value)
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
            return

        total_monthly = sum(bills.values())
        monthly_saving = salary - total_monthly
        yearly_saving = monthly_saving * 12
        yearly_expenses = total_monthly * 12
        net_worth = salary * 12
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        status = (
            "✅ You're saving monthly and growing well!"
            if monthly_saving > 0 else
            "⚠️ Watch your spending! You’re breaking even."
            if monthly_saving == 0 else
            "❌ Overspending! Consider adjusting your budget."
        )

        new_data = {
            "Timestamp": timestamp,
            "Salary": salary,
            **bills,
            "Monthly Expenses": total_monthly,
            "Monthly Savings": monthly_saving,
            "Yearly Net Worth": net_worth,
            "Yearly Expenses": yearly_expenses,
            "Yearly Savings": yearly_saving
        }

        df = pd.DataFrame([new_data])
        filename = "expense_report.xlsx"
        if os.path.exists(filename):
            existing = pd.read_excel(filename)
            updated = pd.concat([existing, df], ignore_index=True)
            updated.to_excel(filename, index=False)
        else:
            df.to_excel(filename, index=False)

        results = f"""
📌 Date: {timestamp}

💼 Monthly Salary: ${salary:,.2f}
📉 Monthly Expenses: ${total_monthly:,.2f}
💰 Monthly Savings: ${monthly_saving:,.2f}

🗓 Yearly Projections:
- Net Worth: ${net_worth:,.2f}
- Expenses: ${yearly_expenses:,.2f}
- Savings: ${yearly_saving:,.2f}

📈 Status: {status}
        """
        self.result_text.delete("1.0", "end")
        self.result_text.insert("1.0", results.strip())

        self.show_charts(bills, salary, monthly_saving)

        # Optional: email report to self or client
        # self.send_email("recipient@example.com", "📊 Financial Report", results.strip())

    def show_charts(self, bills, salary, saving):
        labels = list(bills.keys())
        sizes = list(bills.values())

        fig, axs = plt.subplots(1, 2, figsize=(12, 5))

        axs[0].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        axs[0].axis('equal')
        axs[0].set_title("Monthly Expense Breakdown")

        axs[1].bar(["Salary", "Expenses", "Savings"], [salary, sum(sizes), saving],
                   color=["#4CAF50", "#F44336", "#2196F3"])
        axs[1].set_title("Monthly Financial Comparison")
        axs[1].set_ylabel("Amount ($)")

        plt.tight_layout()
        plt.show()

    def send_email(self, recipient_email, subject, message):
        sender_email = "your-email@gmail.com"
        sender_password = "your-app-password"

        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient_email

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, sender_password)
                server.send_message(msg)
            print("✅ Email sent successfully.")
        except Exception as e:
            print("❌ Email failed:", e)


if __name__ == "__main__":
    root = ttk.Window(themename="litera")
    app = ExpenseTracker(root)
    root.mainloop()
