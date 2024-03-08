from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
users = {}
recipes = {}

@dataclass
class User:
	name: str
	email: str
	recipes: list
	favorites: list

@dataclass
class Recipe:
	name: str
	ingredients: list
	instructions: list
	images: list
	categories: list

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	users[user.email] = user
	return jsonify(user), 201

@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	recipe = Recipe(**data)
	recipes[recipe.name] = recipe
	return jsonify(recipe), 201

@app.route('/recipe', methods=['GET'])
def get_recipes():
	return jsonify(recipes), 200

@app.route('/recipe/<name>', methods=['GET'])
def get_recipe(name):
	recipe = recipes.get(name)
	if recipe:
		return jsonify(recipe), 200
	else:
		return {'message': 'Recipe not found'}, 404

if __name__ == '__main__':
	app.run(debug=True)
