# Import necessary modules
from flask import request, jsonify

# List to store users
users = []

# Function to create an account
def create_account(user):
    # Check if username already exists
    if any(u['username'] == user['username'] for u in users):
        return jsonify({'message': 'Username already exists'}), 400
    # Add user to list
    users.append(user)
    return jsonify({'message': 'Account created successfully'}), 200

# Function to manage account
def manage_account(username, updated_user):
    # Find and update user
    for user in users:
        if user['username'] == username:
            user.update(updated_user)
            return jsonify({'message': 'Account updated successfully'}), 200
    return jsonify({'message': 'User not found'}), 404

# Function to save favorite recipe
def save_favorite_recipe(username, recipe_id):
    # Find user and add recipe to favorites
    for user in users:
        if user['username'] == username:
            user['favorites'].append(recipe_id)
            return jsonify({'message': 'Recipe added to favorites'}), 200
    return jsonify({'message': 'User not found'}), 404

# Function to display profile page
def display_profile(username):
    # Find and return user
    for user in users:
        if user['username'] == username:
            return jsonify(user), 200
    return jsonify({'message': 'User not found'}), 404