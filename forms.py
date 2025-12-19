"""WTForms for the Legal Advocacy Platform."""
from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, BooleanField, SubmitField,
    TextAreaField, SelectField, IntegerField, DateField,
    DateTimeField, FloatField
)
from wtforms.validators import (
    DataRequired, Email, EqualTo, Length, Optional, NumberRange
)


class LoginForm(FlaskForm):
    """User login form."""
    
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    """User registration form."""
    
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=100)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, message='Password must be at least 8 characters long')
    ])
    password2 = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password', message='Passwords must match')
    ])
    phone = StringField('Phone Number', validators=[Optional(), Length(max=20)])
    address = StringField('Address', validators=[Optional(), Length(max=200)])
    city = StringField('City', validators=[Optional(), Length(max=100)])
    state = StringField('State', validators=[Optional(), Length(max=2)])
    zip_code = StringField('ZIP Code', validators=[Optional(), Length(max=10)])
    submit = SubmitField('Register')


class EligibilityForm(FlaskForm):
    """Income eligibility form."""
    
    annual_income = FloatField('Annual Household Income ($)', validators=[
        DataRequired(),
        NumberRange(min=0, message='Income must be a positive number')
    ])
    household_size = IntegerField('Number of People in Household', validators=[
        DataRequired(),
        NumberRange(min=1, message='Household size must be at least 1')
    ])
    submit = SubmitField('Check Eligibility')


class CaseForm(FlaskForm):
    """Case creation form."""
    
    case_type = SelectField('Case Type', validators=[DataRequired()], choices=[
        ('family_law', 'Family Law'),
        ('small_claims', 'Small Claims'),
        ('housing', 'Housing/Eviction'),
        ('immigration', 'Immigration'),
        ('consumer', 'Consumer Rights'),
        ('employment', 'Employment'),
        ('other', 'Other')
    ])
    description = TextAreaField('Case Description', validators=[DataRequired()])
    court_name = StringField('Court Name', validators=[Optional(), Length(max=200)])
    priority = SelectField('Priority', validators=[DataRequired()], choices=[
        ('low', 'Low'),
        ('normal', 'Normal'),
        ('high', 'High'),
        ('urgent', 'Urgent')
    ], default='normal')
    submit = SubmitField('Create Case')


class DocumentForm(FlaskForm):
    """Document generation form."""
    
    case_id = SelectField('Case', coerce=int, validators=[DataRequired()])
    title = StringField('Document Title', validators=[DataRequired(), Length(max=200)])
    submit = SubmitField('Generate Document')


class AppointmentForm(FlaskForm):
    """Appointment scheduling form."""
    
    title = StringField('Appointment Title', validators=[DataRequired(), Length(max=200)])
    description = TextAreaField('Description', validators=[Optional()])
    appointment_date = DateTimeField('Appointment Date & Time', 
                                    format='%Y-%m-%d %H:%M',
                                    validators=[DataRequired()])
    duration_minutes = IntegerField('Duration (minutes)', 
                                   validators=[DataRequired(), NumberRange(min=15, max=480)],
                                   default=60)
    location = StringField('Location', validators=[Optional(), Length(max=200)])
    submit = SubmitField('Schedule Appointment')
