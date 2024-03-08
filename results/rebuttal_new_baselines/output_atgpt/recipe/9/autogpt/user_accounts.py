from flask import request, jsonify

users = []

def create_account(user):
    users.append(user)
    return jsonify({'message': 'Account created successfully'}), 200

def manage_account(user_id, updated_user):
    for user in users:
        if user['id'] == user_id:
            user.update(updated_user)
            return jsonify({'message': 'Account updated successfully'}), 200
    return jsonify({'message': 'Account not found'}), 404

def save_favorite_recipe(user_id, recipe_id):
    for user in users:
        if user['id'] == user_id:
            user['favorites'].append(recipe_id)
            return jsonify({'message': 'Recipe added to favorites'}), 200
    return jsonify({'message': 'Account not found'}), 404

def display_profile(user_id):
    for user in users:
        if user['id'] == user_id:
            return jsonify(user), 200
    return jsonify({'message': 'Account not found'}), 404