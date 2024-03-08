from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

users = {}
recipes = {}

@dataclass
class User:
	name: str
	email: str
	password: str
	recipes: list

@dataclass
class Recipe:
	name: str
	ingredients: list
	instructions: list
	image: str
	category: str

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

@app.route('/recipe/<name>', methods=['GET'])
def get_recipe(name):
	recipe = recipes.get(name)
	if recipe:
		return jsonify(recipe), 200
	else:
		return {'message': 'Recipe not found'}, 404

@app.route('/recipe/<name>', methods=['PUT'])
def update_recipe(name):
	data = request.get_json()
	recipe = recipes.get(name)
	if recipe:
		recipe = Recipe(**data)
		recipes[name] = recipe
		return jsonify(recipe), 200
	else:
		return {'message': 'Recipe not found'}, 404

@app.route('/recipe/<name>', methods=['DELETE'])
def delete_recipe(name):
	recipe = recipes.get(name)
	if recipe:
		del recipes[name]
		return {'message': 'Recipe deleted'}, 200
	else:
		return {'message': 'Recipe not found'}, 404

if __name__ == '__main__':
	app.run(debug=True)
