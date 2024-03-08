from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DB = {
	'users': {},
	'recipes': {},
	'categories': {}
}

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

@dataclass
class Category:
	id: str
	name: str

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

@app.route('/category', methods=['POST'])
def create_category():
	data = request.get_json()
	category = Category(**data)
	DB['categories'][category.id] = category
	return jsonify(category), 201

if __name__ == '__main__':
	app.run(debug=True)
