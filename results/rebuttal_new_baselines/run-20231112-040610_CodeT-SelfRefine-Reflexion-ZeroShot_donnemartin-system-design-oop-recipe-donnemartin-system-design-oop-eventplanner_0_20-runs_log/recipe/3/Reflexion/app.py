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
	username: str
	password: str
	recipes: list
	favorites: list
	following: list

@dataclass
class Recipe:
	id: str
	name: str
	ingredients: list
	instructions: list
	images: list
	category: str
	user_id: str

@dataclass
class Review:
	id: str
	user_id: str
	recipe_id: str
	rating: int
	comment: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	DB['users'][user.id] = user
	return jsonify(user), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = DB['users'].get(data['id'])
	if user and user.password == data['password']:
		return jsonify(user), 200
	return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
	data = request.get_json()
	recipe = Recipe(**data)
	DB['recipes'][recipe.id] = recipe
	DB['users'][recipe.user_id].recipes.append(recipe.id)
	return jsonify(recipe), 201

@app.route('/search_recipe', methods=['GET'])
def search_recipe():
	name = request.args.get('name')
	recipes = [recipe for recipe in DB['recipes'].values() if name in recipe.name]
	return jsonify(recipes), 200

if __name__ == '__main__':
	app.run(debug=True)
