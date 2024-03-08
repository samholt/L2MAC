# Import necessary modules
from flask import request, jsonify

# List to store recipes
recipes = []

# Function to submit a recipe
def submit_recipe(recipe):
    # Validate recipe format
    if 'name' not in recipe or 'ingredients' not in recipe or 'instructions' not in recipe:
        return jsonify({'message': 'Invalid recipe format'}), 400
    # Add recipe to list
    recipes.append(recipe)
    return jsonify({'message': 'Recipe submitted successfully'}), 200

# Function to edit a recipe
def edit_recipe(recipe_id, updated_recipe):
    # Validate recipe format
    if 'name' not in updated_recipe or 'ingredients' not in updated_recipe or 'instructions' not in updated_recipe:
        return jsonify({'message': 'Invalid recipe format'}), 400
    # Find and update recipe
    for recipe in recipes:
        if recipe['id'] == recipe_id:
            recipe.update(updated_recipe)
            return jsonify({'message': 'Recipe updated successfully'}), 200
    return jsonify({'message': 'Recipe not found'}), 404

# Function to delete a recipe
def delete_recipe(recipe_id):
    # Find and delete recipe
    for recipe in recipes:
        if recipe['id'] == recipe_id:
            recipes.remove(recipe)
            return jsonify({'message': 'Recipe deleted successfully'}), 200
    return jsonify({'message': 'Recipe not found'}), 404