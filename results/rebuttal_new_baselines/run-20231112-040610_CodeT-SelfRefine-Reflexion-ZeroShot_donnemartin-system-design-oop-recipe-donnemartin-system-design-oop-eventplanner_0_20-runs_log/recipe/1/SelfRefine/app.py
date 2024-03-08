from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DB = {
	'users': {},
	'recipes': {},
	'reviews': {}
}

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

@dataclass
class Review:
	id: str
	user_id: str
	recipe_id: str
	rating: int
	comment: str

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	DB['users'][user.id] = user
	return jsonify(user), 201

@app.route('/user/<id>', methods=['GET'])
def get_user(id):
	user = DB['users'].get(id)
	if not user:
		return jsonify({'error': 'User not found'}), 404
	return jsonify(user), 200

@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
	data = request.get_json()
	user = DB['users'].get(id)
	if not user:
		return jsonify({'error': 'User not found'}), 404
	user.name = data.get('name', user.name)
	user.recipes = data.get('recipes', user.recipes)
	user.favorites = data.get('favorites', user.favorites)
	return jsonify(user), 200

@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
	user = DB['users'].pop(id, None)
	if not user:
		return jsonify({'error': 'User not found'}), 404
	return jsonify({'message': 'User deleted'}), 200

@app.route('/user/<id>/favorite/<recipe_id>', methods=['POST'])
def favorite_recipe(id, recipe_id):
	user = DB['users'].get(id)
	recipe = DB['recipes'].get(recipe_id)
	if not user or not recipe:
		return jsonify({'error': 'User or Recipe not found'}), 404
	user.favorites.append(recipe_id)
	return jsonify(user), 200

@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	recipe = Recipe(**data)
	DB['recipes'][recipe.id] = recipe
	return jsonify(recipe), 201

@app.route('/recipe/<id>', methods=['GET'])
def get_recipe(id):
	recipe = DB['recipes'].get(id)
	if not recipe:
		return jsonify({'error': 'Recipe not found'}), 404
	return jsonify(recipe), 200

@app.route('/recipe/<id>', methods=['PUT'])
def update_recipe(id):
	data = request.get_json()
	recipe = DB['recipes'].get(id)
	if not recipe:
		return jsonify({'error': 'Recipe not found'}), 404
	recipe.name = data.get('name', recipe.name)
	recipe.ingredients = data.get('ingredients', recipe.ingredients)
	recipe.instructions = data.get('instructions', recipe.instructions)
	recipe.images = data.get('images', recipe.images)
	recipe.categories = data.get('categories', recipe.categories)
	return jsonify(recipe), 200

@app.route('/recipe/<id>', methods=['DELETE'])
def delete_recipe(id):
	recipe = DB['recipes'].pop(id, None)
	if not recipe:
		return jsonify({'error': 'Recipe not found'}), 404
	return jsonify({'message': 'Recipe deleted'}), 200

@app.route('/review', methods=['POST'])
def create_review():
	data = request.get_json()
	review = Review(**data)
	DB['reviews'][review.id] = review
	return jsonify(review), 201

@app.route('/review/<id>', methods=['GET'])
def get_review(id):
	review = DB['reviews'].get(id)
	if not review:
		return jsonify({'error': 'Review not found'}), 404
	return jsonify(review), 200

@app.route('/review/<id>', methods=['PUT'])
def update_review(id):
	data = request.get_json()
	review = DB['reviews'].get(id)
	if not review:
		return jsonify({'error': 'Review not found'}), 404
	review.rating = data.get('rating', review.rating)
	review.comment = data.get('comment', review.comment)
	return jsonify(review), 200

@app.route('/review/<id>', methods=['DELETE'])
def delete_review(id):
	review = DB['reviews'].pop(id, None)
	if not review:
		return jsonify({'error': 'Review not found'}), 404
	return jsonify({'message': 'Review deleted'}), 200

if __name__ == '__main__':
	app.run(debug=True)
