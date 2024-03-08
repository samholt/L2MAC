# Import necessary modules

from flask import request
from entrypoint import db
from werkzeug.security import generate_password_hash, check_password_hash

# Define the User model

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    favorite_recipes = db.Column(db.String(500))

# Function to create an account

def create_account(username, password):
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

# Function to manage account

def manage_account(id, username, password):
    user = User.query.get(id)
    user.username = username
    user.password = generate_password_hash(password)
    db.session.commit()

# Function to save favorite recipes

def save_favorite_recipe(id, recipe_id):
    user = User.query.get(id)
    user.favorite_recipes += ',' + str(recipe_id)
    db.session.commit()

# Function to display profile page

def display_profile(id):
    user = User.query.get(id)
    return user