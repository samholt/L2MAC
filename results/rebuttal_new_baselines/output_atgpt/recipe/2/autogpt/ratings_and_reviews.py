# Import necessary modules

from flask import request
from entrypoint import db
from recipe_management import Recipe

# Define the Review model

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(500), nullable=False)

# Function to rate a recipe

def rate_recipe(recipe_id, user_id, rating):
    new_review = Review(recipe_id=recipe_id, user_id=user_id, rating=rating)
    db.session.add(new_review)
    db.session.commit()

# Function to write a review

def write_review(recipe_id, user_id, review):
    new_review = Review(recipe_id=recipe_id, user_id=user_id, review=review)
    db.session.add(new_review)
    db.session.commit()

# Function to display average rating on recipe page

def display_average_rating(recipe_id):
    reviews = Review.query.filter(Review.recipe_id == recipe_id).all()
    if reviews:
        return sum([review.rating for review in reviews]) / len(reviews)
    return None