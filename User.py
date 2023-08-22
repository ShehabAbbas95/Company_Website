# Importing the required modules
from flask_login import UserMixin , current_user
from flask_sqlalchemy import SQLAlchemy
# initialize the db
db = SQLAlchemy()
# Make a class for our User 
class User(db.Model,UserMixin):
    # Add props to our class
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False)
    mobile = db.Column(db.Integer)
    # Method to update the user email (it takes the new email as an argument)
    def update_email(self,new_email):
        # Get the old email using current_user provided by flask-login
        old_email = current_user.email
        # Get the user saved data and update the email
        user = User.query.filter_by(email=old_email).first()
        user.email = new_email
        db.session.commit()
    def update_username(self,username):
        # Get the old email using current_user provided by flask-login
        # it is better to make quering data and chang as a function to avoid repetition (Refactor it)
        old_email = current_user.email
        user = User.query.filter_by(email=old_email).first()
        user.username = username
        db.session.commit()