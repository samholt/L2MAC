from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import List

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
	recipes: List[str]
	favorites: List[str]
	followers: List[str]

@dataclass
class Recipe:
	id: str
	name: str
	ingredients: List[str]
	instructions: List[str]
	images: List[str]
	categories: List[str]
	reviews: List[str]

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	DB['users'][user.id] = user
	return jsonify(user), 201

@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	recipe = Recipe(**data)
	DB['recipes'][recipe.id] = recipe
	return jsonify(recipe), 201

@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
	user = DB['users'].get(user_id)
	if not user:
		return jsonify({'error': 'User not found'}), 404
	return jsonify(user), 200

@app.route('/recipe/<recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
	recipe = DB['recipes'].get(recipe_id)
	if not recipe:
		return jsonify({'error': 'Recipe not found'}), 404
	return jsonify(recipe), 200

if __name__ == '__main__':
	app.run(debug=True)
