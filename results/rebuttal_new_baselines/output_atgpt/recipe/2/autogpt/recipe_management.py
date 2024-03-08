# Import necessary modules

from flask import request
from entrypoint import db

# Define the Recipe model

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    ingredients = db.Column(db.String(500), nullable=False)
    instructions = db.Column(db.String(500), nullable=False)

# Function to submit a recipe

def submit_recipe(name, ingredients, instructions):
    new_recipe = Recipe(name=name, ingredients=ingredients, instructions=instructions)
    db.session.add(new_recipe)
    db.session.commit()

# Function to edit a recipe

def edit_recipe(id, name, ingredients, instructions):
    recipe = Recipe.query.get(id)
    recipe.name = name
    recipe.ingredients = ingredients
    recipe.instructions = instructions
    db.session.commit()

# Function to delete a recipe

def delete_recipe(id):
    recipe = Recipe.query.get(id)
    db.session.delete(recipe)
    db.session.commit()

# Function to validate the recipe format

def validate_recipe(name, ingredients, instructions):
    if not name or not ingredients or not instructions:
        return False
    return True