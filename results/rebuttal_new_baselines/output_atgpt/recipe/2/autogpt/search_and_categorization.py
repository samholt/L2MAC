# Import necessary modules

from flask import request
from entrypoint import db
from recipe_management import Recipe

# Function to search recipes by name

def search_by_name(name):
    return Recipe.query.filter(Recipe.name.contains(name)).all()

# Function to search recipes by ingredients

def search_by_ingredients(ingredients):
    return Recipe.query.filter(Recipe.ingredients.contains(ingredients)).all()

# Function to categorize recipes by type

def categorize_by_type(type):
    return Recipe.query.filter(Recipe.type == type).all()

# Function to categorize recipes by cuisine

def categorize_by_cuisine(cuisine):
    return Recipe.query.filter(Recipe.cuisine == cuisine).all()

# Function to categorize recipes by dietary needs

def categorize_by_dietary_needs(dietary_needs):
    return Recipe.query.filter(Recipe.dietary_needs == dietary_needs).all()