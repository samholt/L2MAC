from flask import Flask, request, jsonify
from models import User, Recipe
from utils import search_recipes, categorize_recipes

app = Flask(__name__)

@app.route('/create_account', methods=['POST'])
def create_account():
	data = request.get_json()
	user = User(data['username'], data['password'])
	return jsonify({'message': 'Account created successfully'}), 201

@app.route('/change_password', methods=['PUT'])
def change_password():
	data = request.get_json()
	user = User.get_by_username(data['username'])
	if not user:
		return jsonify({'message': 'User not found'}), 404
	user.change_password(data['new_password'])
	return jsonify({'message': 'Password changed successfully'}), 200

@app.route('/save_favorite/<int:recipe_id>', methods=['POST'])
def save_favorite(recipe_id):
	data = request.get_json()
	user = User.get_by_username(data['username'])
	if not user:
		return jsonify({'message': 'User not found'}), 404
	user.save_favorite(recipe_id)
	return jsonify({'message': 'Recipe saved to favorites successfully'}), 200

@app.route('/profile/<string:username>', methods=['GET'])
def profile(username):
	user = User.get_by_username(username)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	profile_data = {
		'submitted_recipes': [recipe.id for recipe in user.submitted_recipes],
		'favorites': user.favorites
	}
	return jsonify(profile_data), 200

@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
	data = request.get_json()
	user = User.get_by_username(data['username'])
	if not user:
		return jsonify({'message': 'User not found'}), 404
	if not Recipe.validate_data(data):
		return jsonify({'message': 'Invalid recipe data'}), 400
	recipe = Recipe(data['title'], data['ingredients'], data['instructions'], data['image'], data['categories'], user)
	user.submit_recipe(recipe)
	return jsonify({'message': 'Recipe submitted successfully'}), 201

@app.route('/edit_recipe/<int:recipe_id>', methods=['PUT'])
def edit_recipe(recipe_id):
	data = request.get_json()
	user = User.get_by_username(data['username'])
	if not user:
		return jsonify({'message': 'User not found'}), 404
	recipe = Recipe.get_by_id(recipe_id)
	if not recipe or recipe.user != user:
		return jsonify({'message': 'Recipe not found or user not authorized'}), 404
	recipe.edit(data)
	return jsonify({'message': 'Recipe edited successfully'}), 200

@app.route('/delete_recipe/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
	data = request.get_json()
	user = User.get_by_username(data['username'])
	if not user:
		return jsonify({'message': 'User not found'}), 404
	recipe = Recipe.get_by_id(recipe_id)
	if not recipe or recipe.user != user:
		return jsonify({'message': 'Recipe not found or user not authorized'}), 404
	recipe.delete()
	return jsonify({'message': 'Recipe deleted successfully'}), 200

@app.route('/search_recipes', methods=['GET'])
def search_recipes_route():
	query = request.args.get('query')
	search_type = request.args.get('type')
	results = search_recipes(query, search_type)
	return jsonify(results), 200

@app.route('/categorize_recipes', methods=['GET'])
def categorize_recipes_route():
	category = request.args.get('category')
	categorization_type = request.args.get('type')
	results = categorize_recipes(category, categorization_type)
	return jsonify(results), 200
