from flask import Flask, request, jsonify
from user import User
from recipe import Recipe
from search import Search
from rating import Rating
from community import Community
from admin import Admin
from recommendation import Recommendation

app = Flask(__name__)

users = {}
recipes = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	password = data['password']
	users[username] = User(username, password)
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username in users and users[username].password == password:
		return jsonify({'message': 'Login successful'}), 200
	else:
		return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
	data = request.get_json()
	name = data['name']
	ingredients = data['ingredients']
	instructions = data['instructions']
	images = data['images']
	category = data['category']
	type = data['type']
	cuisine = data['cuisine']
	diet = data['diet']
	recipe = Recipe(name, ingredients, instructions, images, category, type, cuisine, diet)
	recipes[name] = recipe
	return jsonify({'message': 'Recipe submitted successfully'}), 200

@app.route('/search', methods=['GET'])
def search():
	data = request.args
	search_term = data['search_term']
	search = Search(list(recipes.values()))
	results = search.search_by_name(search_term)
	return jsonify({'results': [recipe.name for recipe in results]}), 200

@app.route('/rate', methods=['POST'])
def rate():
	data = request.get_json()
	username = data['username']
	recipe_name = data['recipe_name']
	rating = data['rating']
	review = data['review']
	if username in users and recipe_name in recipes:
		user = users[username]
		recipe = recipes[recipe_name]
		Rating(user, recipe, rating, review)
		return jsonify({'message': 'Rating submitted successfully'}), 200
	else:
		return jsonify({'message': 'Invalid username or recipe name'}), 400

@app.route('/recommend', methods=['GET'])
def recommend():
	username = request.args.get('username')
	if username in users:
		user = users[username]
		recommendation = Recommendation(user, list(recipes.values()))
		recommended_recipes = recommendation.generate_recommendations()
		return jsonify({'recommended_recipes': [recipe.name for recipe in recommended_recipes]}), 200
	else:
		return jsonify({'message': 'Invalid username'}), 400

if __name__ == '__main__':
	app.run(debug=True)
