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

@dataclass
class Recipe:
	name: str
	ingredients: str
	instructions: str
	image: str
	category: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username in users:
		return jsonify({'message': 'User already exists'}), 400
	users[username] = User(username, password)
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
	data = request.get_json()
	username = data['username']
	recipe_name = data['recipe_name']
	ingredients = data['ingredients']
	instructions = data['instructions']
	image = data['image']
	category = data['category']
	if username not in users:
		return jsonify({'message': 'User does not exist'}), 400
	recipes[recipe_name] = Recipe(recipe_name, ingredients, instructions, image, category)
	return jsonify({'message': 'Recipe submitted successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
