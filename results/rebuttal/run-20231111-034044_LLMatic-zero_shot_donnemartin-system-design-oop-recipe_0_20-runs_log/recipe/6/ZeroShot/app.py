from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DB = {}

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
	DB[user.id] = user
	return jsonify(user), 201

@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
	user = DB.get(user_id)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	return jsonify(user), 200

@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	recipe = Recipe(**data)
	DB[recipe.id] = recipe
	return jsonify(recipe), 201

@app.route('/recipe/<recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
	recipe = DB.get(recipe_id)
	if not recipe:
		return jsonify({'message': 'Recipe not found'}), 404
	return jsonify(recipe), 200

if __name__ == '__main__':
	app.run(debug=True)
