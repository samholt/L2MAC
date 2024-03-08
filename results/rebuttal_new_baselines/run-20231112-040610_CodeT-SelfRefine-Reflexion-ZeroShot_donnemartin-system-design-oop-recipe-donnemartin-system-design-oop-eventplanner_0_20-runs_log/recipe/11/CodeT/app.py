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
	id: int
	name: str
	ingredients: list
	instructions: list
	images: list
	categories: list
	reviews: list

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username in users:
		return jsonify({'message': 'User already exists'}), 400
	users[username] = User(username, password, [], [])
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
	data = request.get_json()
	username = data['username']
	recipe = data['recipe']
	if username not in users:
		return jsonify({'message': 'User does not exist'}), 400
	recipe_id = len(recipes) + 1
	recipes[recipe_id] = Recipe(recipe_id, recipe['name'], recipe['ingredients'], recipe['instructions'], recipe['images'], recipe['categories'], [])
	users[username].recipes.append(recipe_id)
	return jsonify({'message': 'Recipe submitted successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
