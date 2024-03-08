from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DB = {
	'users': {},
	'recipes': {}
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
	reviews: list

@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
	data = request.get_json()
	recipe = Recipe(**data)
	DB['recipes'][recipe.id] = recipe
	return jsonify({'message': 'Recipe submitted successfully'}), 200

@app.route('/edit_recipe/<recipe_id>', methods=['PUT'])
def edit_recipe(recipe_id):
	data = request.get_json()
	recipe = DB['recipes'].get(recipe_id)
	if recipe:
		for key, value in data.items():
			setattr(recipe, key, value)
		return jsonify({'message': 'Recipe updated successfully'}), 200
	return jsonify({'message': 'Recipe not found'}), 404

@app.route('/delete_recipe/<recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
	recipe = DB['recipes'].pop(recipe_id, None)
	if recipe:
		return jsonify({'message': 'Recipe deleted successfully'}), 200
	return jsonify({'message': 'Recipe not found'}), 404

@app.route('/search_recipes', methods=['GET'])
def search_recipes():
	query = request.args.get('query')
	results = [recipe for recipe in DB['recipes'].values() if query in recipe.name or query in recipe.categories]
	return jsonify(results), 200

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	DB['users'][user.id] = user
	return jsonify({'message': 'User created successfully'}), 200

@app.route('/rate_recipe/<recipe_id>', methods=['POST'])
def rate_recipe(recipe_id):
	data = request.get_json()
	recipe = DB['recipes'].get(recipe_id)
	if recipe:
		recipe.reviews.append(data)
		return jsonify({'message': 'Rating submitted successfully'}), 200
	return jsonify({'message': 'Recipe not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
