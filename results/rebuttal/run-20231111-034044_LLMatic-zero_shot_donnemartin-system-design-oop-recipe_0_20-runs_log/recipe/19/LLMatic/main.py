from flask import Flask, request
from user import User
from recipe import Recipe
from review import Review
from category import Category
from admin import Admin
from search import Search
from recommendation import Recommendation
from feed import Feed

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/create_account', methods=['POST'])
def create_account():
	data = request.get_json()
	user = User(data['username'], data['password'])
	user.create_account(data['username'], data['password'])
	return 'Account created successfully', 200

@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
	data = request.get_json()
	recipe = Recipe(data['name'], data['ingredients'], data['instructions'], data['images'], data['categories'])
	recipe.submit_recipe()
	return 'Recipe submitted successfully', 200

@app.route('/search', methods=['GET'])
def search():
	data = request.get_json()
	search = Search()
	results = search.search_by_name(data['name'])
	return {'results': results}, 200

if __name__ == '__main__':
	app.run(debug=True)
