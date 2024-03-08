from flask import Flask, render_template, request
from user import User
from recipe import Recipe
from search import Search
from rating import Rating
from admin import Admin

app = Flask(__name__)

# Mock database
recipe_db = [
	{'name': 'Recipe 1', 'ingredients': ['Ingredient 1', 'Ingredient 2'], 'instructions': ['Step 1', 'Step 2'], 'images': ['Image 1', 'Image 2'], 'categories': ['Category 1', 'Category 2']},
	{'name': 'Recipe 2', 'ingredients': ['Ingredient 3', 'Ingredient 4'], 'instructions': ['Step 3', 'Step 4'], 'images': ['Image 3', 'Image 4'], 'categories': ['Category 3', 'Category 4']}
]

@app.route('/')
def home():
	return 'Welcome to Home Page'

@app.route('/user', methods=['GET', 'POST'])
def user():
	if request.method == 'POST':
		user = User('User 1', 'Password 1')
		return 'User Page'
	return 'User Page'

@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
	if request.method == 'POST':
		recipe = Recipe('Recipe 1', ['Ingredient 1', 'Ingredient 2'], ['Step 1', 'Step 2'], ['Image 1', 'Image 2'], ['Category 1', 'Category 2'])
		return 'Recipe Page'
	return 'Recipe Page'

@app.route('/search')
def search():
	search = Search(recipe_db)
	return 'Search Page'

@app.route('/rating')
def rating():
	rating = Rating('User 1', 'Recipe 1', 5, 'Great recipe!')
	return 'Rating Page'

@app.route('/admin')
def admin():
	admin = Admin()
	return 'Admin Page'

if __name__ == '__main__':
	app.run(debug=True)
