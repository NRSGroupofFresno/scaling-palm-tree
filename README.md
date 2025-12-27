# Legal Advocacy Platform

A comprehensive web-based platform providing free legal advocacy and authorized representative services for low-income families. This platform offers self-help resources for court documents, case management, appointment scheduling, and document generation.

## Overview

The Legal Advocacy Platform is operated by **NRS Group of Fresno** and serves as the parent company for multiple community-focused initiatives. We provide free legal services to eligible low-income families, including:

- 🏛️ Legal representation and advocacy
- 📄 Court document preparation and assistance
- 👨‍👩‍👧‍👦 Family law support
- 🏠 Housing and eviction defense
- 💼 Employment rights assistance
- 🤝 Free consultations for eligible families

## Features

### User Management
- User registration and authentication
- Profile management with income verification
- Eligibility checking for free services

### Case Management
- Create and track legal cases
- Multiple case types (family law, housing, immigration, etc.)
- Case status tracking and priority management
- Document attachment and case notes

### Document Generation
- Pre-built templates for common legal documents
- Automated document generation with user information
- Support for various document types:
  - Petition for Name Change
  - Small Claims Complaint
  - Request for Fee Waiver
  - And more...

### Appointment Scheduling
- Schedule consultations and appointments
- Track upcoming appointments
- Location and duration management

### Eligibility Verification
- Income-based eligibility checking
- Household size consideration
- Automatic qualification determination

## Technology Stack

- **Backend**: Python Flask
- **Database**: SQLAlchemy with SQLite (development) / PostgreSQL (production)
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF with WTForms
- **Frontend**: HTML5, CSS3, JavaScript
- **Testing**: Python unittest

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/NRSGroupofFresno/scaling-palm-tree.git
cd scaling-palm-tree
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and set your SECRET_KEY and other configuration
```

5. Initialize the database:
```bash
python -c "from app import create_app; from models import db; app = create_app(); app.app_context().push(); db.create_all()"
```

6. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Usage

### For Users

1. **Register**: Create an account with your personal information
2. **Check Eligibility**: Submit your household income and size to verify eligibility
3. **Create Cases**: Start a new case for your legal matter
4. **Generate Documents**: Use document templates to create legal forms
5. **Schedule Appointments**: Book consultations with advocates

### Income Eligibility Guidelines

You may qualify for free services if your annual household income is:
- 1 person: $30,000 or less
- 2 people: $40,000 or less
- 3 people: $50,000 or less
- 4 people: $60,000 or less
- 5+ people: Add $10,000 per additional person

## Testing

Run the test suite:
```bash
python tests.py
```

Or with verbose output:
```bash
python -m unittest tests -v
```

## Project Structure

```
scaling-palm-tree/
├── app.py                 # Main Flask application
├── models.py              # Database models
├── forms.py               # WTForms form definitions
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── tests.py              # Unit tests
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── cases.html
│   ├── documents.html
│   ├── appointments.html
│   └── ...
├── static/               # Static assets
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
└── README.md
```

## Development

### Adding New Document Templates

To add a new document template, edit the `initialize_templates()` function in `app.py`:

```python
{
    'name': 'Template Name',
    'category': 'Category',
    'description': 'Description',
    'content': '''Template content with {PLACEHOLDERS}'''
}
```

Available placeholders:
- `{FIRST_NAME}`, `{LAST_NAME}` - User's name
- `{ADDRESS}`, `{CITY}`, `{STATE}`, `{ZIP}` - User's address
- `{DATE}` - Current date

### Extending Case Types

Case types can be modified in `forms.py` in the `CaseForm` class:

```python
case_type = SelectField('Case Type', choices=[
    ('type_id', 'Type Name'),
    ...
])
```

## Security

- Passwords are hashed using Werkzeug's security utilities
- CSRF protection enabled on all forms
- SQL injection protection through SQLAlchemy ORM
- Input validation on all user inputs

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is dedicated to serving low-income families and communities in need.

## Contact

**NRS Group of Fresno**
- Email: info@nrsgroup.org
- Phone: (559) 555-0100
- Address: 123 Main Street, Fresno, CA 93721

## Acknowledgments

This platform is built to serve the community and provide accessible legal resources to those who need them most. We are committed to helping low-income families navigate the legal system with dignity and support.
