from flask import request, jsonify

recipes = []

def submit_recipe(recipe):
    recipes.append(recipe)
    return jsonify({'message': 'Recipe submitted successfully'}), 200

def edit_recipe(recipe_id, updated_recipe):
    for recipe in recipes:
        if recipe['id'] == recipe_id:
            recipe.update(updated_recipe)
            return jsonify({'message': 'Recipe updated successfully'}), 200
    return jsonify({'message': 'Recipe not found'}), 404

def delete_recipe(recipe_id):
    for recipe in recipes:
        if recipe['id'] == recipe_id:
            recipes.remove(recipe)
            return jsonify({'message': 'Recipe deleted successfully'}), 200
    return jsonify({'message': 'Recipe not found'}), 404

def validate_recipe_format(recipe):
    required_fields = ['id', 'name', 'ingredients', 'instructions']
    if not all(field in recipe for field in required_fields):
        return False
    return True