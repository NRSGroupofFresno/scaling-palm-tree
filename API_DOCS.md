# API Documentation

## Overview

This document describes the routes and functionality available in the Legal Advocacy Platform.

## Authentication

The platform uses Flask-Login for session-based authentication. Users must log in to access protected routes.

### Registration
- **URL**: `/register`
- **Method**: `GET`, `POST`
- **Auth Required**: No
- **Description**: Create a new user account

**POST Parameters:**
```json
{
  "first_name": "string",
  "last_name": "string",
  "email": "string",
  "password": "string",
  "password2": "string",
  "phone": "string (optional)",
  "address": "string (optional)",
  "city": "string (optional)",
  "state": "string (optional)",
  "zip_code": "string (optional)"
}
```

### Login
- **URL**: `/login`
- **Method**: `GET`, `POST`
- **Auth Required**: No
- **Description**: Authenticate user

**POST Parameters:**
```json
{
  "email": "string",
  "password": "string",
  "remember_me": "boolean"
}
```

### Logout
- **URL**: `/logout`
- **Method**: `GET`
- **Auth Required**: Yes
- **Description**: End user session

## User Routes

### Dashboard
- **URL**: `/dashboard`
- **Method**: `GET`
- **Auth Required**: Yes
- **Description**: User's main dashboard with overview of cases and appointments

### Check Eligibility
- **URL**: `/eligibility`
- **Method**: `GET`, `POST`
- **Auth Required**: Yes
- **Description**: Verify income eligibility for free services

**POST Parameters:**
```json
{
  "annual_income": "float",
  "household_size": "integer"
}
```

**Response**: Updates user's eligibility status

## Case Management

### List Cases
- **URL**: `/cases`
- **Method**: `GET`
- **Auth Required**: Yes
- **Description**: View all cases for the logged-in user

### Create Case
- **URL**: `/case/new`
- **Method**: `GET`, `POST`
- **Auth Required**: Yes
- **Description**: Create a new legal case

**POST Parameters:**
```json
{
  "case_type": "string",
  "description": "string",
  "court_name": "string (optional)",
  "priority": "string"
}
```

**Case Types:**
- `family_law`
- `small_claims`
- `housing`
- `immigration`
- `consumer`
- `employment`
- `other`

**Priority Levels:**
- `low`
- `normal`
- `high`
- `urgent`

### View Case
- **URL**: `/case/<int:case_id>`
- **Method**: `GET`
- **Auth Required**: Yes
- **Description**: View details of a specific case
- **Permissions**: User must own the case

## Document Management

### List Document Templates
- **URL**: `/documents`
- **Method**: `GET`
- **Auth Required**: Yes
- **Description**: Browse available document templates grouped by category

### Generate Document
- **URL**: `/document/generate/<int:template_id>`
- **Method**: `GET`, `POST`
- **Auth Required**: Yes
- **Description**: Generate a document from a template

**POST Parameters:**
```json
{
  "case_id": "integer",
  "title": "string"
}
```

**Available Placeholders in Templates:**
- `{FIRST_NAME}` - User's first name
- `{LAST_NAME}` - User's last name
- `{ADDRESS}` - User's address
- `{CITY}` - User's city
- `{STATE}` - User's state
- `{ZIP}` - User's ZIP code
- `{DATE}` - Current date

## Appointment Management

### List Appointments
- **URL**: `/appointments`
- **Method**: `GET`
- **Auth Required**: Yes
- **Description**: View all appointments for the logged-in user

### Create Appointment
- **URL**: `/appointment/new`
- **Method**: `GET`, `POST`
- **Auth Required**: Yes
- **Description**: Schedule a new appointment

**POST Parameters:**
```json
{
  "title": "string",
  "description": "string (optional)",
  "appointment_date": "datetime (YYYY-MM-DD HH:MM)",
  "duration_minutes": "integer",
  "location": "string (optional)"
}
```

## Information Pages

### Home
- **URL**: `/`
- **Method**: `GET`
- **Auth Required**: No
- **Description**: Platform home page

### About
- **URL**: `/about`
- **Method**: `GET`
- **Auth Required**: No
- **Description**: Information about the organization and services

### Contact
- **URL**: `/contact`
- **Method**: `GET`
- **Auth Required**: No
- **Description**: Contact information

## Data Models

### User
```python
{
  "id": "integer",
  "email": "string (unique)",
  "first_name": "string",
  "last_name": "string",
  "phone": "string",
  "address": "string",
  "city": "string",
  "state": "string",
  "zip_code": "string",
  "annual_income": "float",
  "household_size": "integer",
  "is_eligible": "boolean",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

### Case
```python
{
  "id": "integer",
  "user_id": "integer (foreign key)",
  "case_number": "string (unique)",
  "case_type": "string",
  "description": "text",
  "status": "string",
  "priority": "string",
  "court_name": "string",
  "filing_date": "date",
  "hearing_date": "date",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

### Document
```python
{
  "id": "integer",
  "case_id": "integer (foreign key)",
  "title": "string",
  "document_type": "string",
  "file_path": "string",
  "template_name": "string",
  "content": "text",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

### Appointment
```python
{
  "id": "integer",
  "user_id": "integer (foreign key)",
  "title": "string",
  "description": "text",
  "appointment_date": "datetime",
  "duration_minutes": "integer",
  "location": "string",
  "status": "string",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

## Status Codes

- `200 OK` - Request successful
- `302 Found` - Redirect (common after form submission)
- `400 Bad Request` - Invalid input
- `401 Unauthorized` - Authentication required
- `403 Forbidden` - Access denied
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error

## Error Handling

Errors are displayed to users via flash messages with categories:
- `success` - Operation completed successfully
- `info` - Informational message
- `warning` - Warning message
- `danger` - Error message

## Security Features

1. **Password Hashing**: All passwords are hashed using Werkzeug's security utilities
2. **CSRF Protection**: Enabled on all forms via Flask-WTF
3. **SQL Injection Protection**: SQLAlchemy ORM prevents SQL injection
4. **Input Validation**: All user inputs are validated
5. **Session Management**: Secure session handling via Flask-Login

## Rate Limiting

Currently not implemented. Consider adding for production:
- Login attempts: 5 per minute
- API calls: 100 per hour per user
- Registration: 3 per hour per IP

## Future Enhancements

Potential API additions:
- RESTful API endpoints for mobile app integration
- Webhook support for external integrations
- OAuth2 authentication for third-party access
- Document upload functionality
- Real-time notifications
- Email integration for appointment reminders
- SMS notifications
- Payment processing for non-eligible users
