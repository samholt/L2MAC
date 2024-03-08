from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
users = {}
recipes = {}

@dataclass
class User:
	id: str
	name: str
	recipes: list

@dataclass
class Recipe:
	id: str
	name: str
	ingredients: list
	instructions: list
	image: str
	categories: list

@app.route('/users', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	users[user.id] = user
	return jsonify(user), 201

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
	user = users.get(id)
	if not user:
		return {'error': 'User not found'}, 404
	return jsonify(user), 200

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
	data = request.get_json()
	user = users.get(id)
	if not user:
		return {'error': 'User not found'}, 404
	user.name = data.get('name', user.name)
	user.recipes = data.get('recipes', user.recipes)
	return jsonify(user), 200

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
	user = users.get(id)
	if not user:
		return {'error': 'User not found'}, 404
	del users[id]
	return {'message': 'User deleted'}, 200

@app.route('/recipes', methods=['POST'])
def create_recipe():
	data = request.get_json()
	recipe = Recipe(**data)
	recipes[recipe.id] = recipe
	return jsonify(recipe), 201

@app.route('/recipes/<id>', methods=['GET'])
def get_recipe(id):
	recipe = recipes.get(id)
	if not recipe:
		return {'error': 'Recipe not found'}, 404
	return jsonify(recipe), 200

@app.route('/recipes/<id>', methods=['PUT'])
def update_recipe(id):
	data = request.get_json()
	recipe = recipes.get(id)
	if not recipe:
		return {'error': 'Recipe not found'}, 404
	recipe.name = data.get('name', recipe.name)
	recipe.ingredients = data.get('ingredients', recipe.ingredients)
	recipe.instructions = data.get('instructions', recipe.instructions)
	recipe.image = data.get('image', recipe.image)
	recipe.categories = data.get('categories', recipe.categories)
	return jsonify(recipe), 200

@app.route('/recipes/<id>', methods=['DELETE'])
def delete_recipe(id):
	recipe = recipes.get(id)
	if not recipe:
		return {'error': 'Recipe not found'}, 404
	del recipes[id]
	return {'message': 'Recipe deleted'}, 200

if __name__ == '__main__':
	app.run(debug=True)
