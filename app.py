"""Main Flask application for Legal Advocacy Platform."""
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from datetime import datetime
import os

from models import db, User, Case, Document, Appointment, DocumentTemplate
from config import Config
from forms import (
    LoginForm, RegistrationForm, CaseForm, DocumentForm, 
    AppointmentForm, EligibilityForm
)


def create_app(config_class=Config):
    """Application factory pattern."""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    login_manager.login_message = 'Please log in to access this page.'
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Create database tables
    with app.app_context():
        db.create_all()
        initialize_templates()
    
    # Routes
    @app.route('/')
    def index():
        """Home page."""
        return render_template('index.html')
    
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        """User registration."""
        if current_user.is_authenticated:
            return redirect(url_for('dashboard'))
        
        form = RegistrationForm()
        if form.validate_on_submit():
            user = User(
                email=form.email.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                phone=form.phone.data,
                address=form.address.data,
                city=form.city.data,
                state=form.state.data,
                zip_code=form.zip_code.data
            )
            user.set_password(form.password.data)
            
            db.session.add(user)
            db.session.commit()
            
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        
        return render_template('register.html', form=form)
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        """User login."""
        if current_user.is_authenticated:
            return redirect(url_for('dashboard'))
        
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            
            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                next_page = request.args.get('next')
                return redirect(next_page or url_for('dashboard'))
            else:
                flash('Invalid email or password.', 'danger')
        
        return render_template('login.html', form=form)
    
    @app.route('/logout')
    @login_required
    def logout():
        """User logout."""
        logout_user()
        flash('You have been logged out.', 'info')
        return redirect(url_for('index'))
    
    @app.route('/dashboard')
    @login_required
    def dashboard():
        """User dashboard."""
        cases = Case.query.filter_by(user_id=current_user.id).order_by(Case.created_at.desc()).all()
        appointments = Appointment.query.filter_by(user_id=current_user.id).filter(
            Appointment.appointment_date >= datetime.now()
        ).order_by(Appointment.appointment_date).limit(5).all()
        
        return render_template('dashboard.html', cases=cases, appointments=appointments)
    
    @app.route('/eligibility', methods=['GET', 'POST'])
    @login_required
    def eligibility():
        """Check income eligibility."""
        form = EligibilityForm()
        
        if form.validate_on_submit():
            current_user.annual_income = form.annual_income.data
            current_user.household_size = form.household_size.data
            
            # Check eligibility
            threshold = app.config['LOW_INCOME_THRESHOLD'].get(
                min(form.household_size.data, 5),
                70000 + (form.household_size.data - 5) * 10000
            )
            
            current_user.is_eligible = form.annual_income.data <= threshold
            db.session.commit()
            
            if current_user.is_eligible:
                flash('You qualify for free legal assistance!', 'success')
            else:
                flash('Based on your income, you may not qualify for free services. Please contact us for other options.', 'warning')
            
            return redirect(url_for('dashboard'))
        
        # Pre-fill form with existing data
        if current_user.annual_income:
            form.annual_income.data = current_user.annual_income
            form.household_size.data = current_user.household_size
        
        return render_template('eligibility.html', form=form)
    
    @app.route('/cases')
    @login_required
    def cases():
        """List all cases for the user."""
        user_cases = Case.query.filter_by(user_id=current_user.id).order_by(Case.created_at.desc()).all()
        return render_template('cases.html', cases=user_cases)
    
    @app.route('/case/new', methods=['GET', 'POST'])
    @login_required
    def new_case():
        """Create a new case."""
        form = CaseForm()
        
        if form.validate_on_submit():
            case = Case(
                user_id=current_user.id,
                case_type=form.case_type.data,
                description=form.description.data,
                court_name=form.court_name.data,
                priority=form.priority.data
            )
            
            # Generate case number
            case.case_number = f"CASE-{datetime.now().year}-{Case.query.count() + 1:05d}"
            
            db.session.add(case)
            db.session.commit()
            
            flash('Case created successfully!', 'success')
            return redirect(url_for('view_case', case_id=case.id))
        
        return render_template('new_case.html', form=form)
    
    @app.route('/case/<int:case_id>')
    @login_required
    def view_case(case_id):
        """View a specific case."""
        case = Case.query.get_or_404(case_id)
        
        # Ensure user owns this case
        if case.user_id != current_user.id:
            flash('You do not have permission to view this case.', 'danger')
            return redirect(url_for('cases'))
        
        return render_template('view_case.html', case=case)
    
    @app.route('/documents')
    @login_required
    def documents():
        """List document templates."""
        templates = DocumentTemplate.query.order_by(DocumentTemplate.category, DocumentTemplate.name).all()
        
        # Group by category
        categories = {}
        for template in templates:
            if template.category not in categories:
                categories[template.category] = []
            categories[template.category].append(template)
        
        return render_template('documents.html', categories=categories)
    
    @app.route('/document/generate/<int:template_id>', methods=['GET', 'POST'])
    @login_required
    def generate_document(template_id):
        """Generate a document from a template."""
        template = DocumentTemplate.query.get_or_404(template_id)
        form = DocumentForm()
        
        # Get user's cases for the dropdown
        form.case_id.choices = [(c.id, f"{c.case_number} - {c.case_type}") 
                                for c in Case.query.filter_by(user_id=current_user.id).all()]
        
        if form.validate_on_submit():
            # Replace placeholders in template
            content = template.template_content
            content = content.replace('{FIRST_NAME}', current_user.first_name)
            content = content.replace('{LAST_NAME}', current_user.last_name)
            content = content.replace('{ADDRESS}', current_user.address or '')
            content = content.replace('{CITY}', current_user.city or '')
            content = content.replace('{STATE}', current_user.state or '')
            content = content.replace('{ZIP}', current_user.zip_code or '')
            content = content.replace('{DATE}', datetime.now().strftime('%B %d, %Y'))
            
            document = Document(
                case_id=form.case_id.data,
                title=form.title.data,
                document_type=template.name,
                template_name=template.name,
                content=content
            )
            
            db.session.add(document)
            db.session.commit()
            
            flash('Document generated successfully!', 'success')
            return redirect(url_for('view_case', case_id=form.case_id.data))
        
        return render_template('generate_document.html', template=template, form=form)
    
    @app.route('/appointments')
    @login_required
    def appointments():
        """List all appointments."""
        user_appointments = Appointment.query.filter_by(user_id=current_user.id).order_by(
            Appointment.appointment_date.desc()
        ).all()
        return render_template('appointments.html', appointments=user_appointments)
    
    @app.route('/appointment/new', methods=['GET', 'POST'])
    @login_required
    def new_appointment():
        """Schedule a new appointment."""
        form = AppointmentForm()
        
        if form.validate_on_submit():
            appointment = Appointment(
                user_id=current_user.id,
                title=form.title.data,
                description=form.description.data,
                appointment_date=form.appointment_date.data,
                duration_minutes=form.duration_minutes.data,
                location=form.location.data
            )
            
            db.session.add(appointment)
            db.session.commit()
            
            flash('Appointment scheduled successfully!', 'success')
            return redirect(url_for('appointments'))
        
        return render_template('new_appointment.html', form=form)
    
    @app.route('/about')
    def about():
        """About page."""
        return render_template('about.html')
    
    @app.route('/contact')
    def contact():
        """Contact page."""
        return render_template('contact.html')
    
    return app


def initialize_templates():
    """Initialize default document templates."""
    templates = [
        {
            'name': 'Petition for Name Change',
            'category': 'Family Law',
            'description': 'Petition to legally change your name',
            'content': '''PETITION FOR NAME CHANGE

IN THE SUPERIOR COURT OF CALIFORNIA
COUNTY OF FRESNO

Petitioner: {FIRST_NAME} {LAST_NAME}
Address: {ADDRESS}, {CITY}, {STATE} {ZIP}
Date: {DATE}

TO THE HONORABLE COURT:

I, {FIRST_NAME} {LAST_NAME}, respectfully petition this Court for an order changing my name.

1. Current legal name: {FIRST_NAME} {LAST_NAME}
2. Proposed new name: [NEW NAME]
3. Reason for name change: [REASON]

WHEREFORE, Petitioner prays that this Court grant an order changing their name as requested.

Dated: {DATE}

_____________________________
{FIRST_NAME} {LAST_NAME}
Petitioner
'''
        },
        {
            'name': 'Small Claims Complaint',
            'category': 'Small Claims',
            'description': 'File a small claims case',
            'content': '''SMALL CLAIMS COMPLAINT

PLAINTIFF: {FIRST_NAME} {LAST_NAME}
Address: {ADDRESS}, {CITY}, {STATE} {ZIP}

DEFENDANT: [DEFENDANT NAME]
Address: [DEFENDANT ADDRESS]

1. Plaintiff claims from defendant the sum of $[AMOUNT]
2. Date of incident: [DATE OF INCIDENT]
3. Description of claim:
[DESCRIPTION OF CLAIM]

4. I have asked defendant to pay this money, but it has not been paid.
5. I understand that by filing this claim, I may not sue in another court.

Dated: {DATE}

_____________________________
{FIRST_NAME} {LAST_NAME}
Plaintiff
'''
        },
        {
            'name': 'Request for Fee Waiver',
            'category': 'Fee Waiver',
            'description': 'Request to waive court fees',
            'content': '''REQUEST FOR FEE WAIVER

IN THE SUPERIOR COURT OF CALIFORNIA
COUNTY OF FRESNO

Applicant: {FIRST_NAME} {LAST_NAME}
Address: {ADDRESS}, {CITY}, {STATE} {ZIP}

I request that the court waive court fees and costs because I cannot afford to pay them.

HOUSEHOLD INCOME INFORMATION:
Monthly gross income: $[MONTHLY INCOME]
Number of people in household: [HOUSEHOLD SIZE]

I declare under penalty of perjury under the laws of the State of California that the foregoing is true and correct.

Dated: {DATE}

_____________________________
{FIRST_NAME} {LAST_NAME}
'''
        }
    ]
    
    for template_data in templates:
        existing = DocumentTemplate.query.filter_by(name=template_data['name']).first()
        if not existing:
            template = DocumentTemplate(
                name=template_data['name'],
                category=template_data['category'],
                description=template_data['description'],
                template_content=template_data['content']
            )
            db.session.add(template)
    
    db.session.commit()


if __name__ == '__main__':
    app = create_app()
    # Only enable debug mode in development environment
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
