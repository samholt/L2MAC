from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import List

app = Flask(__name__)

# Mock database
DB = {
	'users': {},
	'recipes': {}
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
	reviews: List[str]
	average_rating: float

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

if __name__ == '__main__':
	app.run(debug=True)
