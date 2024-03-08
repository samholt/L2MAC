from flask import Flask, request
from user import User
from recipe import Recipe
from review import Review
from category import Category
from admin import Admin
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
	return user.create_account(data['username'], data['password'], data['preferences'])

@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
	data = request.get_json()
	recipe = Recipe(data['name'], data['category'], data['instructions'], data['submitted_by'])
	return 'Recipe submitted successfully'

@app.route('/search_recipe', methods=['GET'])
def search_recipe():
	data = request.get_json()
	recipe = Recipe(data['name'], data['category'], data['instructions'], data['submitted_by'])
	return 'Recipe search completed'

if __name__ == '__main__':
	app.run(debug=True)
