from flask import Flask, request, jsonify
from users import UserManager
from recipes import RecipeManager
from reviews import Review
from categories import Category
from admin import manage_recipes, remove_content
from recommendations import RecommendationManager
from database import MockDatabase

app = Flask(__name__)

db = MockDatabase()

user_manager = UserManager(db)
recipe_manager = RecipeManager(db)
review_manager = Review(db)
category_manager = Category(db)
recommendation_manager = RecommendationManager(db)

@app.route('/users', methods=['POST'])
def create_user():
	data = request.get_json()
	user = user_manager.create_user(data['id'], data['name'], data['email'])
	return jsonify(user.__dict__), 201

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def handle_user(id):
	if request.method == 'GET':
		user = user_manager.get_user(id)
		return jsonify(user.__dict__), 200
	elif request.method == 'DELETE':
		message = user_manager.delete_user(id)
		return jsonify({'message': message}), 200

@app.route('/recipes', methods=['POST'])
def submit_recipe():
	data = request.get_json()
	recipe = recipe_manager.submit_recipe(data['recipe_id'], data['user_id'], data['title'], data['description'], data['ingredients'], data['category'])
	return jsonify(recipe), 201

@app.route('/recipes/<recipe_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_recipe(recipe_id):
	if request.method == 'GET':
		recipe = recipe_manager.get_recipe(recipe_id)
		return jsonify(recipe), 200
	elif request.method == 'PUT':
		data = request.get_json()
		message = recipe_manager.edit_recipe(recipe_id, data.get('title'), data.get('description'), data.get('ingredients'), data.get('category'))
		return jsonify({'message': message}), 200
	elif request.method == 'DELETE':
		message = recipe_manager.delete_recipe(recipe_id)
		return jsonify({'message': message}), 200

@app.route('/reviews', methods=['POST'])
def add_review():
	data = request.get_json()
	response = review_manager.add_review(data['user_id'], data['recipe_id'], data['rating'], data['review'])
	return jsonify(response), 201

@app.route('/reviews/<recipe_id>', methods=['GET'])
def get_reviews(recipe_id):
	response = review_manager.get_reviews(recipe_id)
	return jsonify(response), 200

@app.route('/categories', methods=['POST'])
def add_category():
	data = request.get_json()
	category_manager.add_category(data['category_name'], data['recipe_id'])
	return jsonify({'message': 'Category added successfully'}), 201

@app.route('/categories/<category_name>', methods=['GET'])
def get_recipes_by_category(category_name):
	recipes = category_manager.get_recipes_by_category(category_name)
	return jsonify(recipes), 200

@app.route('/admin/recipes', methods=['GET'])
def get_all_recipes():
	recipes = recipe_manager.get_all_recipes()
	return jsonify(recipes), 200

@app.route('/admin/recipes/<recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
	message = recipe_manager.delete_recipe(recipe_id)
	return jsonify({'message': message}), 200

@app.route('/recommendations/<user_id>', methods=['GET'])
def get_recommendations(user_id):
	recommendations = recommendation_manager.get_recommendations(user_id)
	if recommendations is None:
		return jsonify([]), 200
	return jsonify(recommendations), 200

if __name__ == '__main__':
	app.run(debug=True)
