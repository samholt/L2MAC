from flask import Flask, request
from user import User
from recipe import Recipe
from review import Review
from admin import Admin

app = Flask(__name__)

users = {}
recipes = {}
reviews = {}
admin = Admin('admin', 'admin')

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/create_account', methods=['POST'])
def create_account():
	data = request.get_json()
	username = data['username']
	password = data['password']
	user = User(username, password)
	users[username] = user
	return 'Account created successfully'

@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
	data = request.get_json()
	username = data['username']
	recipe_name = data['recipe_name']
	recipe = Recipe(recipe_name, [], [], [], '')
	user = users[username]
	user.submitted_recipes.append(recipe)
	recipes[recipe_name] = recipe
	return 'Recipe submitted successfully'

@app.route('/rate_recipe', methods=['POST'])
def rate_recipe():
	data = request.get_json()
	username = data['username']
	recipe_name = data['recipe_name']
	rating = data['rating']
	review = Review(users[username], recipes[recipe_name], rating)
	reviews[(username, recipe_name)] = review
	return 'Recipe rated successfully'

@app.route('/admin_manage_recipes', methods=['POST'])
def admin_manage_recipes():
	data = request.get_json()
	recipe_id = data['recipe_id']
	action = data['action']
	admin.manage_recipes(recipe_id, action)
	return 'Admin managed recipes successfully'

if __name__ == '__main__':
	app.run(debug=True)
