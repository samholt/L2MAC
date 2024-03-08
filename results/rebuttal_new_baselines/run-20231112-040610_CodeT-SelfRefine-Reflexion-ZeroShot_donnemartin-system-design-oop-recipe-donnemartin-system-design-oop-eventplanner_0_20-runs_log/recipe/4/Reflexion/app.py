from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
users = {}
recipes = {}

@dataclass
class User:
	username: str
	password: str
	recipes: list
	favorites: list

@dataclass
class Recipe:
	name: str
	ingredients: list
	instructions: list
	images: list
	categories: list

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username in users:
		return jsonify({'message': 'User already exists'}), 400
	users[username] = User(username, password, [], [])
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username not in users or users[username].password != password:
		return jsonify({'message': 'Invalid username or password'}), 400
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
	data = request.get_json()
	username = data['username']
	recipe = Recipe(data['name'], data['ingredients'], data['instructions'], data['images'], data['categories'])
	if username not in users:
		return jsonify({'message': 'User does not exist'}), 400
	users[username].recipes.append(recipe)
	recipes[recipe.name] = recipe
	return jsonify({'message': 'Recipe submitted successfully'}), 200

@app.route('/delete_recipe', methods=['DELETE'])
def delete_recipe():
	data = request.get_json()
	username = data['username']
	recipe_name = data['recipe_name']
	if username not in users or recipe_name not in recipes:
		return jsonify({'message': 'User or recipe does not exist'}), 400
	if recipe_name not in users[username].recipes:
		return jsonify({'message': 'User did not submit this recipe'}), 400
	users[username].recipes.remove(recipe_name)
	recipes.pop(recipe_name)
	return jsonify({'message': 'Recipe deleted successfully'}), 200

@app.route('/edit_recipe', methods=['PUT'])
def edit_recipe():
	data = request.get_json()
	username = data['username']
	recipe_name = data['recipe_name']
	new_recipe = Recipe(data['new_name'], data['new_ingredients'], data['new_instructions'], data['new_images'], data['new_categories'])
	if username not in users or recipe_name not in recipes:
		return jsonify({'message': 'User or recipe does not exist'}), 400
	if recipe_name not in users[username].recipes:
		return jsonify({'message': 'User did not submit this recipe'}), 400
	users[username].recipes.remove(recipe_name)
	users[username].recipes.append(new_recipe)
	recipes.pop(recipe_name)
	recipes[new_recipe.name] = new_recipe
	return jsonify({'message': 'Recipe edited successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
