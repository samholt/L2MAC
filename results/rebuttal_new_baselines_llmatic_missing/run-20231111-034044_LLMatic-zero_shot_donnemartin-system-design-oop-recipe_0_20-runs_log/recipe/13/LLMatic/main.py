from flask import Flask, request, jsonify
from user import User, Profile
from recipe import Recipe, RecipeValidator
from search import Search
from category import Category
from rating import Rating
from review import Review
from follow import Follow
from feed import Feed
from admin import Admin
from statistics import Statistics
from recommendation import Recommendation
from notification import Notification

app = Flask(__name__)

# Mock database
users = {}
recipes = {}

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(data['username'], data['password'], data['email'])
	users[data['username']] = user
	return jsonify({'message': 'User created successfully.'}), 201

@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	recipe = Recipe(data['name'], data['ingredients'], data['instructions'], data['images'], data['categories'])
	if RecipeValidator.validate(recipe):
		recipes[data['name']] = recipe
		return jsonify({'message': 'Recipe created successfully.'}), 201
	else:
		return jsonify({'message': 'Invalid recipe data.'}), 400

@app.route('/search', methods=['GET'])
def search():
	data = request.args
	search = Search(recipes.values())
	if 'name' in data:
		result = search.search_by_name(data['name'])
	elif 'ingredient' in data:
		result = search.search_by_ingredient(data['ingredient'])
	elif 'category' in data:
		result = search.search_by_category(data['category'])
	else:
		return jsonify({'message': 'Invalid search parameters.'}), 400
	return jsonify({'result': [recipe.name for recipe in result]}), 200

if __name__ == '__main__':
	app.run(debug=True)
