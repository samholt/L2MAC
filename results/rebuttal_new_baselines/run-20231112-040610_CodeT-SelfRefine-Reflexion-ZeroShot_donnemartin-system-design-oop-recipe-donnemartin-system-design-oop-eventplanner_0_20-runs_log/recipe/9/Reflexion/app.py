from flask import Flask, request
from dataclasses import dataclass

app = Flask(__name__)

users = {}
recipes = {}
reviews = {}

@dataclass
class User:
	name: str
	email: str

@dataclass
class Recipe:
	title: str
	instructions: str
	ingredients: str
	user: User

@dataclass
class Review:
	user: User
	recipe: Recipe
	comment: str

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(name=data['name'], email=data['email'])
	users[user.email] = user
	return {'message': 'User created successfully'}, 201

@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	user = users.get(data['user_email'])
	recipe = Recipe(title=data['title'], instructions=data['instructions'], ingredients=data['ingredients'], user=user)
	recipes[recipe.title] = recipe
	return {'message': 'Recipe created successfully'}, 201

@app.route('/review', methods=['POST'])
def create_review():
	data = request.get_json()
	user = users.get(data['user_email'])
	recipe = recipes.get(data['recipe_title'])
	review = Review(user=user, recipe=recipe, comment=data['comment'])
	reviews[(user.email, recipe.title)] = review
	return {'message': 'Review created successfully'}, 201

if __name__ == '__main__':
	app.run(debug=True)
