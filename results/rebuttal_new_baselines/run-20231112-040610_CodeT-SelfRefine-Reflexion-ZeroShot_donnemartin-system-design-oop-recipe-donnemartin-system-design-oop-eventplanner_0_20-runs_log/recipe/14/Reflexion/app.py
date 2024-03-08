from flask import Flask, request
from models import User, Recipe, Review

app = Flask(__name__)

users = {}
recipes = {}
reviews = {}

@app.route('/user', methods=['POST'])
def create_user():
	user = User(**request.json)
	users[user.id] = user
	return {'id': user.id}, 201

@app.route('/recipe', methods=['POST'])
def create_recipe():
	recipe = Recipe(**request.json)
	recipes[recipe.id] = recipe
	return {'id': recipe.id}, 201

@app.route('/review', methods=['POST'])
def create_review():
	review = Review(**request.json)
	reviews[review.id] = review
	return {'id': review.id}, 201

@app.route('/user/<int:user_id>/favorite', methods=['POST'])
def add_favorite(user_id):
	recipe_id = request.json['recipe_id']
	users[user_id].favorite_recipes.append(recipe_id)
	return {}, 204
