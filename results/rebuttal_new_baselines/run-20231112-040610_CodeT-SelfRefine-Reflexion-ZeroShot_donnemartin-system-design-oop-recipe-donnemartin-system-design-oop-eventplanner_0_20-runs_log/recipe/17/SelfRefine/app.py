from flask import Flask, request, jsonify
from dataclasses import dataclass, field
from typing import List

app = Flask(__name__)

# Mock database
users = {}
recipes = {}

@dataclass
class User:
	id: str
	name: str
	recipes: List[str] = field(default_factory=list)
	favorites: List[str] = field(default_factory=list)

@dataclass
class Recipe:
	id: str
	name: str
	ingredients: List[str]
	instructions: List[str]
	images: List[str]
	categories: List[str]
	reviews: List[str] = field(default_factory=list)

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	users[user.id] = user
	return jsonify(user), 201

@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	recipe = Recipe(**data)
	recipes[recipe.id] = recipe
	return jsonify(recipe), 201

@app.route('/recipe/<recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
	data = request.get_json()
	recipe = recipes.get(recipe_id)
	if not recipe:
		return {'message': 'Recipe not found'}, 404
	for key, value in data.items():
		setattr(recipe, key, value)
	return jsonify(recipe), 200

@app.route('/recipe/<recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
	recipe = recipes.get(recipe_id)
	if not recipe:
		return {'message': 'Recipe not found'}, 404
	del recipes[recipe_id]
	return {'message': 'Recipe deleted'}, 200

@app.route('/recipe/search', methods=['GET'])
def search_recipe():
	query = request.args.get('q')
	results = [recipe for recipe in recipes.values() if query in recipe.name or query in recipe.ingredients or query in recipe.categories]
	return jsonify(results), 200

@app.route('/user/<user_id>/favorites', methods=['POST'])
def add_favorite(user_id):
	recipe_id = request.get_json().get('recipe_id')
	user = users.get(user_id)
	if not user:
		return {'message': 'User not found'}, 404
	user.favorites.append(recipe_id)
	return jsonify(user), 200

@app.route('/user/<user_id>/recipes', methods=['GET'])
def get_user_recipes(user_id):
	user = users.get(user_id)
	if not user:
		return {'message': 'User not found'}, 404
	user_recipes = [recipes[recipe_id] for recipe_id in user.recipes]
	return jsonify(user_recipes), 200

@app.route('/recipe/<recipe_id>/review', methods=['POST'])
def add_review(recipe_id):
	review = request.get_json().get('review')
	recipe = recipes.get(recipe_id)
	if not recipe:
		return {'message': 'Recipe not found'}, 404
	recipe.reviews.append(review)
	return jsonify(recipe), 200

if __name__ == '__main__':
	app.run(debug=True)
