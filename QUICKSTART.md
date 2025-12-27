# Quick Start Guide

Get the Legal Advocacy Platform up and running in 5 minutes!

## Prerequisites

- Python 3.8 or higher installed
- pip (Python package manager)
- Basic command line knowledge

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/NRSGroupofFresno/scaling-palm-tree.git
cd scaling-palm-tree
```

### 2. Set Up Virtual Environment

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
cp .env.example .env
```

Edit `.env` (optional for quick start - defaults will work):
```
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///legal_advocacy.db
FLASK_ENV=development
```

### 5. Initialize Database

```bash
python -c "from app import create_app; from models import db; app = create_app(); app.app_context().push(); db.create_all()"
```

### 6. Run the Application

```bash
python app.py
```

The application will be available at: **http://localhost:5000**

## First Steps

### 1. Create an Account
- Navigate to http://localhost:5000/register
- Fill in your information
- Create your account

### 2. Check Eligibility
- Log in with your credentials
- Go to "Check Eligibility" in the menu
- Enter your household income and size
- See if you qualify for free services

### 3. Create a Case
- Click "New Case" from the dashboard
- Select your case type
- Enter case details
- Submit

### 4. Generate Documents
- Go to "Documents" in the menu
- Browse available templates
- Select a template
- Fill in the required information
- Generate your document

### 5. Schedule an Appointment
- Click "Schedule Appointment"
- Enter appointment details
- Save

## Common Issues

### Port 5000 Already in Use

If you get an error that port 5000 is already in use:

```bash
# On macOS/Linux
lsof -ti:5000 | xargs kill -9

# Or run on a different port
python -c "from app import create_app; app = create_app(); app.run(port=5001)"
```

### Module Not Found Error

Make sure your virtual environment is activated:

```bash
# You should see (venv) in your terminal prompt
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### Database Errors

If you encounter database errors, recreate the database:

```bash
rm legal_advocacy.db
python -c "from app import create_app; from models import db; app = create_app(); app.app_context().push(); db.create_all()"
```

## Testing

Run the test suite to verify everything is working:

```bash
python -m unittest tests -v
```

You should see:
```
Ran 10 tests in X seconds

OK
```

## What's Next?

- Read the full [README.md](README.md) for detailed information
- Check [SETUP.md](SETUP.md) for production deployment
- Review [API_DOCS.md](API_DOCS.md) for API reference
- Read [SECURITY.md](SECURITY.md) for security guidelines

## Features to Try

### Case Management
- Create different types of cases (family law, housing, immigration, etc.)
- Add notes to your cases
- Attach documents

### Document Templates
Available templates include:
- Petition for Name Change
- Small Claims Complaint
- Request for Fee Waiver

### Appointment System
- Schedule consultations
- Track upcoming appointments
- Add locations and notes

## Getting Help

If you need assistance:

- **Email**: info@nrsgroup.org
- **Phone**: (559) 555-0100
- **Issues**: Open a GitHub issue for bugs or feature requests

## Contributing

We welcome contributions! See [README.md](README.md) for contribution guidelines.

## Demo Credentials

For testing purposes, you can create a test account with:
- Email: test@example.com
- Password: (your chosen password)
- Income: $25,000
- Household Size: 2

This will qualify for free services.

## Tips

1. **Check Eligibility First**: Complete the eligibility check to see all features
2. **Use Templates**: Don't start from scratch - use our document templates
3. **Track Everything**: Keep all case information in one place
4. **Schedule Early**: Book appointments in advance
5. **Keep Records**: Save copies of all generated documents

## Shutting Down

To stop the application:
1. Press `Ctrl+C` in the terminal where the app is running
2. Deactivate virtual environment: `deactivate`

## Next Time

To run the app again:
```bash
cd scaling-palm-tree
source venv/bin/activate  # or venv\Scripts\activate on Windows
python app.py
```

That's it! You're ready to use the Legal Advocacy Platform. 🎉
