
# 💼 Project Name: WealthWise - Pro Financial Tracker

> *Your All-in-One Expense, Savings & Financial Growth Analyzer – Business-Ready, Beautifully Designed.*

## 📊 Overview

**WealthWise** is a professional-grade, Python-powered financial tracker tailored for individuals, entrepreneurs, and small businesses. Designed with simplicity, elegance, and marketing readiness in mind, it empowers users to:

- ✅ Monitor monthly expenses
- ✅ Track savings and net worth
- ✅ Visualize financial growth (via charts)
- ✅ Export reports to Excel
- ✅ Share reports via email or Google Drive
- ✅ Use light/dark modes for accessibility
- ✅ Generate printable PDFs
- ✅ Use it as a standalone `.exe` for testing or deployment

## 🛠 Features

- **Modern GUI** with Light/Dark mode toggle
- **Smart Expense Categorization**: Rent, Food, Transportation, etc.
- **Annual & Monthly Summary** with Net Worth projection
- **Growth Analysis**: Appreciate or depreciate comparison
- **Excel Export** (fully formatted)
- **PDF/Printable Reports** (optional)
- **Email Reports** (optional)
- **Google Drive Backup** (optional)
- **Business Beta Testing Ready** – Package into a standalone `.exe` for distribution

## 📸 Screenshots

| Light Mode 💡 | Dark Mode 🌙 |
|--------------|--------------|
| ![Light](assets/screenshots/light_mode.png) | ![Dark](assets/screenshots/dark_mode.png) |

## 💻 Technologies Used

- `Python 3.10+`
- `ttkbootstrap` for modern UI
- `Matplotlib` & `Pandas` for charts
- `Openpyxl` for Excel export
- `Fpdf2` (optional) for PDF generation
- `smtplib` (optional) for email reports
- `PyInstaller` for packaging into `.exe`

## 🚀 Setup Instructions

### 🔧 Install Requirements

```bash
pip install -r requirements.txt
```

### ▶️ Run the App

```bash
python pro_financial_tracker.py
```

### 📦 Build Executable (Optional)

```bash
pyinstaller --noconfirm --onefile --windowed --icon=icon.ico pro_financial_tracker.py
```

## 📁 File Structure

```
📦 WealthWise/
├── pro_financial_tracker.py
├── requirements.txt
├── icon.ico
├── README.md
├── assets/
│   └── screenshots/
└── dist/
    └── pro_financial_tracker.exe
```

## 💡 Future Add-ons

- 🔐 Google Drive cloud sync
- 🖨 PDF/Printable report builder
- 📆 Monthly tracker with calendar navigation
- 📈 Investment & savings forecast AI
- 💬 User feedback & issue reporting form

## 🧪 For Beta Testers

If you're testing the `.exe` version:
1. Download from the **`/dist/`** folder
2. Run `pro_financial_tracker.exe`
3. Submit feedback through the integrated form or email

## 📬 Contact & Feedback

Have a suggestion or spotted a bug? Open an issue or email us at **finance@wealthwise.app** (placeholder).
