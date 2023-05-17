from flask_sqlalchemy import SQLAlchemy
from project.database import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    username = db.Column(db.String(128))
    password = db.Column(db.String(128))

    def __init__(self, first_name, last_name, email, username, password):
        self.first_name = first_name
        self.last_name =  last_name
        self.email = email
        self.username = username
        self.password = password
    
    def __repr__(self):
        return '<Name Object %r>' % self.id