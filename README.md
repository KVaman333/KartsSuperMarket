# Kart's SuperMarket: Store Management System

A Django web dashboard for running the day-to-day back office of a supermarket: logging receipts and petty cash, writing off damaged inventory, and generating printable vouchers. I built it in 2021 for friends and family to use in their store.

## Features

- **Secure login:** staff sign in with their own accounts, and records are stamped with the logged-in user (for example, the "Paid by" field on petty cash vouchers).
- **Receipts:** record expenses such as water, electricity and freight with amount, payment method and remarks. Each entry gets a serial number so the paper receipt can be matched to its digital record.
- **Petty cash vouchers:** enter amount, charge account, payee and remarks, then print a voucher for signature and filing.
- **Inventory write-off:** log damaged, expired or lost stock by UPC, event type, pack size, quantity, unit price and responsible person.
- **Printable documents:** vouchers and records can be exported as PDFs (xhtml2pdf and ReportLab).
- **Nav-bar driven workflow:** each task (Receipt, Inventory Write-off, Accounts, and so on) is one click away from any page.
- **Cloud data layer:** Firebase Admin SDK and Cloud Firestore integration alongside Django's default SQLite database.
- **Production-ready setup:** configured for deployment with Gunicorn and WhiteNoise on a Procfile-based host.

## Tech Stack

| Area | Technology |
|---|---|
| Language | Python 3.9.7 |
| Framework | Django 3.2.7 |
| Databases | SQLite (default), Google Cloud Firestore via `firebase-admin` |
| PDF generation | xhtml2pdf, ReportLab, PyPDF2 |
| Image handling | Pillow |
| Static files | WhiteNoise |
| Server | Gunicorn |

## Project Structure

```
.
├── KartsSuperMarket/    # Django project settings, URLs, WSGI
├── authentication/      # Login and session handling
├── accounts/            # Receipts, petty cash and accounting features
├── administrator/       # Administrator-side features
├── dashboard/           # Main dashboard
├── functions/           # Shared helper functions
├── tables/              # Table and record views
├── templates/           # HTML templates
├── static/              # CSS, JavaScript and images
├── media/               # Uploaded files
├── manage.py
├── Procfile             # Gunicorn start command for deployment
├── runtime.txt          # Python version for deployment
└── requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.9 (the project is pinned to 3.9.7, and some pinned packages may not build on newer Python versions)
- `pip` and `venv`
- A Firebase project and service-account key, if you want the Firestore features to work

### Installation

```bash
git clone https://github.com/KVaman333/KartsSuperMarket.git
cd KartsSuperMarket

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Mac / Linux

pip install -r requirements.txt
```

### Configure Firebase

Download a service-account key from your Firebase console and keep it **outside version control** (add it to `.gitignore`). Point the app at it using the setting or environment variable your configuration expects.

### Run the app

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open **http://127.0.0.1:8000** in your browser and sign in.

## Deployment

The repo includes a `Procfile` (`web: gunicorn KartsSuperMarket.wsgi`) and a `runtime.txt`, so it can be deployed to Heroku-style platforms. Static files are served with WhiteNoise.

## Known Limitations

- Dependencies are pinned to 2021 versions (Django 3.2, Python 3.9) and should be upgraded before any new production use.
- The project has no automated tests yet.

## Author

**Kunal Vaman Dwivedi**
[GitHub](https://github.com/KVaman333) · [LinkedIn](https://linkedin.com/in/kunal-vaman-285200436)
