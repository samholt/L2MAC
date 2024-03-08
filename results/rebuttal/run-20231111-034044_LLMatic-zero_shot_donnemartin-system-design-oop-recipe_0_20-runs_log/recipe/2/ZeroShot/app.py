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
	favorites: list

@dataclass
class Recipe:
	id: str
	name: str
	ingredients: list
	instructions: list
	images: list
	categories: list
	reviews: list

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
	if recipe:
		recipe.name = data.get('name', recipe.name)
		recipe.ingredients = data.get('ingredients', recipe.ingredients)
		recipe.instructions = data.get('instructions', recipe.instructions)
		recipe.images = data.get('images', recipe.images)
		recipe.categories = data.get('categories', recipe.categories)
		return jsonify(recipe), 200
	else:
		return {'message': 'Recipe not found'}, 404

@app.route('/recipe/<recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
	recipe = recipes.get(recipe_id)
	if recipe:
		del recipes[recipe_id]
		return {'message': 'Recipe deleted'}, 200
	else:
		return {'message': 'Recipe not found'}, 404

if __name__ == '__main__':
	app.run(debug=True)
