"""Application configuration."""
import os
from pathlib import Path

basedir = Path(__file__).parent


class Config:
    """Base configuration."""
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f'sqlite:///{basedir / "legal_advocacy.db"}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Application settings
    APP_NAME = 'Legal Advocacy Platform'
    ITEMS_PER_PAGE = 20
    
    # Income thresholds for eligibility (annual income in USD)
    LOW_INCOME_THRESHOLD = {
        1: 30000,  # Single person
        2: 40000,  # 2 people
        3: 50000,  # 3 people
        4: 60000,  # 4 people
        5: 70000,  # 5+ people (per additional person add $10k)
    }
