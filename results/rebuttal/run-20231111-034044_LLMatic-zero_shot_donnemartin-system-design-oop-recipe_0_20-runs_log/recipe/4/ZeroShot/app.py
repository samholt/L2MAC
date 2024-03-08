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
	user = User(data['name'], data['email'], [], [])
	users[data['email']] = user
	return jsonify(user), 201

@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	recipe = Recipe(data['name'], data['ingredients'], data['instructions'], data['images'], data['categories'])
	recipes[data['name']] = recipe
	return jsonify(recipe), 201

if __name__ == '__main__':
	app.run(debug=True)
