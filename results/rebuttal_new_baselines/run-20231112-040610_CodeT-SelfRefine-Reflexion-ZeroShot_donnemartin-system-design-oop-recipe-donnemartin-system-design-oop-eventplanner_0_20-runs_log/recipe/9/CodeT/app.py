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
	user = User(id=data['id'], name=data['name'], recipes=[], favorites=[])
	users[user.id] = user
	return jsonify(user), 201

@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	recipe = Recipe(id=data['id'], name=data['name'], ingredients=data['ingredients'], instructions=data['instructions'], images=data['images'], categories=data['categories'], reviews=[])
	recipes[recipe.id] = recipe
	return jsonify(recipe), 201

@app.route('/recipe/<recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
	data = request.get_json()
	recipe = recipes[recipe_id]
	recipe.name = data.get('name', recipe.name)
	recipe.ingredients = data.get('ingredients', recipe.ingredients)
	recipe.instructions = data.get('instructions', recipe.instructions)
	recipe.images = data.get('images', recipe.images)
	recipe.categories = data.get('categories', recipe.categories)
	return jsonify(recipe), 200

@app.route('/recipe/<recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
	del recipes[recipe_id]
	return '', 204

@app.route('/recipe/search', methods=['GET'])
def search_recipe():
	query = request.args.get('q')
	results = [recipe for recipe in recipes.values() if query in recipe.name or query in recipe.ingredients or query in recipe.categories]
	return jsonify(results), 200

@app.route('/user/<user_id>/favorites', methods=['POST'])
def add_favorite(user_id):
	recipe_id = request.get_json()['id']
	user = users[user_id]
	user.favorites.append(recipe_id)
	return jsonify(user), 200

@app.route('/user/<user_id>/favorites', methods=['DELETE'])
def remove_favorite(user_id):
	recipe_id = request.get_json()['id']
	user = users[user_id]
	user.favorites.remove(recipe_id)
	return jsonify(user), 200

@app.route('/recipe/<recipe_id>/review', methods=['POST'])
def add_review(recipe_id):
	review = request.get_json()
	recipe = recipes[recipe_id]
	recipe.reviews.append(review)
	return jsonify(recipe), 200

if __name__ == '__main__':
	app.run(debug=True)
