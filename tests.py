"""Unit tests for Legal Advocacy Platform."""
import unittest
from datetime import datetime
from app import create_app
from models import db, User, Case, Document, Appointment, DocumentTemplate
from config import Config


class TestConfig(Config):
    """Test configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False


class BaseTestCase(unittest.TestCase):
    """Base test case with app setup."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    
    def tearDown(self):
        """Clean up after tests."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


class UserModelTestCase(BaseTestCase):
    """Test User model."""
    
    def test_password_hashing(self):
        """Test password hashing and verification."""
        user = User(email='test@example.com', first_name='Test', last_name='User')
        user.set_password('password123')
        
        self.assertTrue(user.check_password('password123'))
        self.assertFalse(user.check_password('wrongpassword'))
    
    def test_user_creation(self):
        """Test creating a user."""
        user = User(
            email='test@example.com',
            first_name='Test',
            last_name='User',
            annual_income=25000,
            household_size=2
        )
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()
        
        self.assertEqual(User.query.count(), 1)
        self.assertEqual(user.email, 'test@example.com')


class CaseModelTestCase(BaseTestCase):
    """Test Case model."""
    
    def test_case_creation(self):
        """Test creating a case."""
        user = User(email='test@example.com', first_name='Test', last_name='User')
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()
        
        case = Case(
            user_id=user.id,
            case_number='CASE-2025-00001',
            case_type='family_law',
            description='Test case',
            status='pending'
        )
        db.session.add(case)
        db.session.commit()
        
        self.assertEqual(Case.query.count(), 1)
        self.assertEqual(case.user_id, user.id)
        self.assertEqual(user.cases[0], case)


class AuthenticationTestCase(BaseTestCase):
    """Test authentication routes."""
    
    def test_registration(self):
        """Test user registration."""
        response = self.client.post('/register', data={
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'password': 'password123',
            'password2': 'password123'
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.query.count(), 1)
    
    def test_login(self):
        """Test user login."""
        user = User(email='test@example.com', first_name='Test', last_name='User')
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()
        
        response = self.client.post('/login', data={
            'email': 'test@example.com',
            'password': 'password123',
            'remember_me': False
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)


class EligibilityTestCase(BaseTestCase):
    """Test eligibility checking."""
    
    def test_eligibility_calculation(self):
        """Test income eligibility calculation."""
        user = User(email='test@example.com', first_name='Test', last_name='User')
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()
        
        # Log in
        self.client.post('/login', data={
            'email': 'test@example.com',
            'password': 'password123'
        })
        
        # Test eligible income
        response = self.client.post('/eligibility', data={
            'annual_income': 25000,
            'household_size': 1
        }, follow_redirects=True)
        
        user = User.query.first()
        self.assertTrue(user.is_eligible)
        
        # Test ineligible income
        response = self.client.post('/eligibility', data={
            'annual_income': 100000,
            'household_size': 1
        }, follow_redirects=True)
        
        user = User.query.first()
        self.assertFalse(user.is_eligible)


class RouteTestCase(BaseTestCase):
    """Test application routes."""
    
    def test_index_route(self):
        """Test index page loads."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_about_route(self):
        """Test about page loads."""
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
    
    def test_contact_route(self):
        """Test contact page loads."""
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)
    
    def test_protected_routes_require_login(self):
        """Test that protected routes redirect to login."""
        protected_routes = ['/dashboard', '/cases', '/appointments', '/eligibility']
        
        for route in protected_routes:
            response = self.client.get(route)
            self.assertEqual(response.status_code, 302)
            self.assertIn('/login', response.location)


if __name__ == '__main__':
    unittest.main()
