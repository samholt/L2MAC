from flask import Flask, request
from .models import User, Recipe, Rating, Review, Admin

app = Flask(__name__)

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User.create(**data)
	return {'id': user.id}, 201

@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	recipe = Recipe.create(**data)
	return {'id': recipe.id}, 201

@app.route('/rating', methods=['POST'])
def create_rating():
	data = request.get_json()
	rating = Rating.create(**data)
	return {'id': rating.id}, 201

@app.route('/review', methods=['POST'])
def create_review():
	data = request.get_json()
	review = Review.create(**data)
	return {'id': review.id}, 201

@app.route('/admin', methods=['POST'])
def create_admin():
	data = request.get_json()
	admin = Admin.create(**data)
	return {'id': admin.id}, 201
