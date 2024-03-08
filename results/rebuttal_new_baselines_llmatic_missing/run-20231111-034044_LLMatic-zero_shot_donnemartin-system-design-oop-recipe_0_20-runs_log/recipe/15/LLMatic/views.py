from flask import Flask, request, jsonify
from services import UserService, RecipeService

app = Flask(__name__)

user_service = UserService()
recipe_service = RecipeService()

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	result = user_service.create_user(**data)
	return jsonify(result.to_json()), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	result = user_service.get_user(data['username'])
	return jsonify(result.to_json()), 200

@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
	data = request.get_json()
	user = user_service.get_user(data['submitted_by'])
	if user is None:
		return jsonify({'error': 'User not found'}), 404
	data['submitted_by'] = user.username
	result = recipe_service.create_recipe(**data)
	return jsonify(result.to_json()), 200

@app.route('/manage_recipe', methods=['POST'])
def manage_recipe():
	data = request.get_json()
	user = user_service.get_user(data['submitted_by'])
	if user is None:
		return jsonify({'error': 'User not found'}), 404
	data['submitted_by'] = user.username
	result = recipe_service.update_recipe(**data)
	if result is None:
		return jsonify({'error': 'Recipe not found'}), 404
	return jsonify(result.to_json()), 200

@app.route('/search', methods=['GET'])
def search():
	data = request.args
	result = recipe_service.get_recipe(data['name'])
	if result is None:
		return jsonify({'error': 'Recipe not found'}), 404
	return jsonify(result.to_json()), 200

@app.route('/profile', methods=['GET', 'POST'])
def profile():
	if request.method == 'POST':
		data = request.get_json()
		result = user_service.update_user(**data)
	else:
		data = request.args
		result = user_service.get_user(data['username'])
	if result is None:
		return jsonify({'error': 'User not found'}), 404
	return jsonify(result.to_json()), 200

@app.route('/save_favorite', methods=['POST'])
def save_favorite():
	data = request.get_json()
	result = user_service.save_favorite_recipe(data['username'], data['recipe_name'])
	if result is None:
		return jsonify({'error': 'Failed to save favorite recipe'}), 400
	return jsonify(result.to_json()), 200

@app.route('/recommendations', methods=['GET'])
def recommendations():
	data = request.args
	user = user_service.get_user(data['username'])
	if user is None:
		return jsonify({'error': 'User not found'}), 404
	result = recipe_service.get_recipe_recommendations(user)
	return jsonify([recipe.to_json() for recipe in result]), 200

# Admin routes
@app.route('/admin/manage_recipes', methods=['GET', 'POST', 'DELETE'])
def manage_recipes():
	if request.method == 'GET':
		result = recipe_service.get_all_recipes()
		return jsonify([recipe.to_json() for recipe in result]), 200
	elif request.method == 'POST':
		data = request.get_json()
		result = recipe_service.update_recipe(**data)
		if result is None:
			return jsonify({'error': 'Recipe not found'}), 404
		return jsonify(result.to_json()), 200
	elif request.method == 'DELETE':
		data = request.get_json()
		result = recipe_service.delete_recipe(data['name'])
		return jsonify({'status': 'success' if result else 'failure'}), 200

@app.route('/admin/site_statistics', methods=['GET'])
def site_statistics():
	user_count = user_service.get_user_count()
	recipe_count = recipe_service.get_recipe_count()
	return jsonify({'user_count': user_count, 'recipe_count': recipe_count}), 200
