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
	user = User(id=data['id'], name=data['name'], recipes=[], favorites=[])
	users[user.id] = user
	return jsonify(user), 201

@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	recipe = Recipe(id=data['id'], name=data['name'], ingredients=data['ingredients'], instructions=data['instructions'], images=data['images'], categories=data['categories'], reviews=[])
	recipes[recipe.id] = recipe
	return jsonify(recipe), 201

if __name__ == '__main__':
	app.run(debug=True)
