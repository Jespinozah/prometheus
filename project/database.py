
"""
Database object for use throughout the application.  Separated into its own file to avoid circular dependencies.
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()