from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
users = {}
recipes = {}

@dataclass
class User:
	id: str
	name: str

@dataclass
class Recipe:
	id: str
	name: str
	ingredients: list
	instructions: list
	image: str
	categories: list

@app.route('/users', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	users[user.id] = user
	return jsonify(user), 201

@app.route('/recipes', methods=['POST'])
def create_recipe():
	data = request.get_json()
	recipe = Recipe(**data)
	recipes[recipe.id] = recipe
	return jsonify(recipe), 201

if __name__ == '__main__':
	app.run(debug=True)
