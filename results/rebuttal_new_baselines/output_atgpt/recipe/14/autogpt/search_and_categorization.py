# Import necessary modules
from flask import request, jsonify

# Function to search recipes by name
def search_by_name(name):
    # Find recipes with matching name
    matching_recipes = [recipe for recipe in recipes if name.lower() in recipe['name'].lower()]
    return jsonify(matching_recipes), 200

# Function to search recipes by ingredient
def search_by_ingredient(ingredient):
    # Find recipes with matching ingredient
    matching_recipes = [recipe for recipe in recipes if ingredient.lower() in recipe['ingredients'].lower()]
    return jsonify(matching_recipes), 200

# Function to categorize recipes by type
def categorize_by_type(type):
    # Find recipes of the specified type
    matching_recipes = [recipe for recipe in recipes if type.lower() == recipe['type'].lower()]
    return jsonify(matching_recipes), 200

# Function to categorize recipes by cuisine
def categorize_by_cuisine(cuisine):
    # Find recipes of the specified cuisine
    matching_recipes = [recipe for recipe in recipes if cuisine.lower() == recipe['cuisine'].lower()]
    return jsonify(matching_recipes), 200

# Function to categorize recipes by dietary needs
def categorize_by_dietary_needs(dietary_needs):
    # Find recipes that meet the specified dietary needs
    matching_recipes = [recipe for recipe in recipes if dietary_needs.lower() in recipe['dietary_needs'].lower()]
    return jsonify(matching_recipes), 200