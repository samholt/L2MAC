from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DB = {
	'users': {},
	'recipes': {},
	'reviews': {}
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
class Review:
	id: str
	user_id: str
	recipe_id: str
	rating: int
	comment: str

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	DB['users'][user.id] = user
	return jsonify(user), 201

@app.route('/user/<id>', methods=['GET'])
def get_user(id):
	user = DB['users'][id]
	return jsonify(user), 200

@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
	data = request.get_json()
	user = User(**data)
	DB['users'][id] = user
	return jsonify(user), 200

@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
	del DB['users'][id]
	return '', 204

@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	recipe = Recipe(**data)
	DB['recipes'][recipe.id] = recipe
	return jsonify(recipe), 201

@app.route('/recipe/<id>', methods=['GET'])
def get_recipe(id):
	recipe = DB['recipes'][id]
	return jsonify(recipe), 200

@app.route('/recipe/<id>', methods=['PUT'])
def update_recipe(id):
	data = request.get_json()
	recipe = Recipe(**data)
	DB['recipes'][id] = recipe
	return jsonify(recipe), 200

@app.route('/recipe/<id>', methods=['DELETE'])
def delete_recipe(id):
	del DB['recipes'][id]
	return '', 204

@app.route('/review', methods=['POST'])
def create_review():
	data = request.get_json()
	review = Review(**data)
	DB['reviews'][review.id] = review
	return jsonify(review), 201

@app.route('/review/<id>', methods=['GET'])
def get_review(id):
	review = DB['reviews'][id]
	return jsonify(review), 200

@app.route('/review/<id>', methods=['PUT'])
def update_review(id):
	data = request.get_json()
	review = Review(**data)
	DB['reviews'][id] = review
	return jsonify(review), 200

@app.route('/review/<id>', methods=['DELETE'])
def delete_review(id):
	del DB['reviews'][id]
	return '', 204

if __name__ == '__main__':
	app.run(debug=True)
