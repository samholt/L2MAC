from flask import Flask, request
from models import User, Recipe, Review
from database import users, recipes, reviews

app = Flask(__name__)

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	users[user.id] = user
	return {'id': user.id}, 201

@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	recipe = Recipe(**data)
	recipes[recipe.id] = recipe
	return {'id': recipe.id}, 201

@app.route('/review', methods=['POST'])
def create_review():
	data = request.get_json()
	review = Review(**data)
	reviews[review.id] = review
	return {'id': review.id}, 201
