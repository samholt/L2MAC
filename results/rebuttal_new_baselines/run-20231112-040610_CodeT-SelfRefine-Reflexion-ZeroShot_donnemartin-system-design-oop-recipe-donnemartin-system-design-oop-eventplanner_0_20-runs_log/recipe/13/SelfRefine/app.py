from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import List

app = Flask(__name__)

# Mock database
DB = {
	'users': {},
	'recipes': {},
	'reviews': {},
	'categories': {}
}

@dataclass
class User:
	id: str
	name: str
	recipes: List[str]
	favorites: List[str]
	followers: List[str]

@dataclass
class Recipe:
	id: str
	name: str
	ingredients: List[str]
	instructions: List[str]
	images: List[str]
	categories: List[str]
	user_id: str

@dataclass
class Review:
	id: str
	user_id: str
	recipe_id: str
	rating: int
	comment: str

@dataclass
class Category:
	id: str
	name: str
	recipes: List[str]

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	DB['users'][user.id] = user
	return jsonify(user), 201

@app.route('/user/<id>', methods=['GET', 'PUT', 'DELETE'])
def handle_user(id):
	if request.method == 'GET':
		return jsonify(DB['users'].get(id)), 200
	elif request.method == 'PUT':
		data = request.get_json()
		for key, value in data.items():
			setattr(DB['users'][id], key, value)
		return jsonify(DB['users'][id]), 200
	elif request.method == 'DELETE':
		del DB['users'][id]
		return '', 204

@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	recipe = Recipe(**data)
	DB['recipes'][recipe.id] = recipe
	return jsonify(recipe), 201

@app.route('/recipe/<id>', methods=['GET', 'PUT', 'DELETE'])
def handle_recipe(id):
	if request.method == 'GET':
		return jsonify(DB['recipes'].get(id)), 200
	elif request.method == 'PUT':
		data = request.get_json()
		for key, value in data.items():
			setattr(DB['recipes'][id], key, value)
		return jsonify(DB['recipes'][id]), 200
	elif request.method == 'DELETE':
		del DB['recipes'][id]
		return '', 204

@app.route('/review', methods=['POST'])
def create_review():
	data = request.get_json()
	review = Review(**data)
	DB['reviews'][review.id] = review
	return jsonify(review), 201

@app.route('/review/<id>', methods=['GET', 'PUT', 'DELETE'])
def handle_review(id):
	if request.method == 'GET':
		return jsonify(DB['reviews'].get(id)), 200
	elif request.method == 'PUT':
		data = request.get_json()
		for key, value in data.items():
			setattr(DB['reviews'][id], key, value)
		return jsonify(DB['reviews'][id]), 200
	elif request.method == 'DELETE':
		del DB['reviews'][id]
		return '', 204

@app.route('/category', methods=['POST'])
def create_category():
	data = request.get_json()
	category = Category(**data)
	DB['categories'][category.id] = category
	return jsonify(category), 201

@app.route('/category/<id>', methods=['GET', 'PUT', 'DELETE'])
def handle_category(id):
	if request.method == 'GET':
		return jsonify(DB['categories'].get(id)), 200
	elif request.method == 'PUT':
		data = request.get_json()
		for key, value in data.items():
			setattr(DB['categories'][id], key, value)
		return jsonify(DB['categories'][id]), 200
	elif request.method == 'DELETE':
		del DB['categories'][id]
		return '', 204

if __name__ == '__main__':
	app.run(debug=True)
