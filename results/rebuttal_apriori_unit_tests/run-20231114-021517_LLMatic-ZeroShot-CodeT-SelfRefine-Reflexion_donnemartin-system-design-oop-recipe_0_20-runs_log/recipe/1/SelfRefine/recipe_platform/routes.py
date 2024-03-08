from flask import Flask, request
from .database import *


app = Flask(__name__)


@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
	data = request.json
	create_recipe(**data)
	return {'status': 'success'}, 200


@app.route('/edit_recipe/<int:recipe_id>', methods=['PUT'])
def edit_recipe(recipe_id):
	data = request.json
	edit_recipe(1, recipe_id, data)
	return {'status': 'success'}, 200


@app.route('/delete_recipe/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
	remove_recipe(1, recipe_id)
	return {'status': 'success'}, 200


@app.route('/search_recipe', methods=['GET'])
def search_recipe():
	query = request.args.get('query')
	results = search_recipes(query)
	return {'results': [recipe.__dict__ for recipe in results]}, 200


@app.route('/search_recipe_by_category', methods=['GET'])
def search_recipe_by_category():
	category = request.args.get('category')
	results = search_recipes_by_category(category)
	return {'results': [recipe.__dict__ for recipe in results]}, 200


@app.route('/submit_rating', methods=['POST'])
def submit_rating():
	data = request.json
	submit_rating(**data)
	return {'status': 'success'}, 200


@app.route('/submit_review', methods=['POST'])
def submit_review():
	data = request.json
	submit_review(**data)
	return {'status': 'success'}, 200


@app.route('/get_reviews/<int:recipe_id>', methods=['GET'])
def get_reviews(recipe_id):
	reviews = get_reviews(recipe_id)
	return {'reviews': [review.__dict__ for review in reviews]}, 200


@app.route('/get_average_rating/<int:recipe_id>', methods=['GET'])
def get_average_rating(recipe_id):
	average_rating = get_average_rating(recipe_id)
	return {'average_rating': average_rating}, 200


@app.route('/follow/<int:followee_id>', methods=['POST'])
def follow(followee_id):
	data = request.json
	follow(data['user_id'], followee_id)
	return {'status': 'success'}, 200


@app.route('/get_feed/<int:user_id>', methods=['GET'])
def get_feed(user_id):
	activities = get_activities(user_id)
	return {'feed': [activity.__dict__ for activity in activities]}, 200
