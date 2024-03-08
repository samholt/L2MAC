from flask import Flask, request, jsonify
from users import create_user, get_user, delete_user
from recipes import Recipe
from reviews import Review
from categories import Categories
from admin import Admin
from recommendations import Recommendations

app = Flask(__name__)

recipe = Recipe()
review = Review()
categories = Categories()
admin = Admin()
recommendations = Recommendations()

@app.route('/user', methods=['POST'])
def create_user_route():
	data = request.get_json()
	user = create_user(data['username'], data['password'])
	return jsonify(user.username), 201

@app.route('/user/<username>', methods=['GET'])
def get_user_route(username):
	user = get_user(username)
	if user:
		return jsonify(user.username), 200
	else:
		return jsonify('User not found'), 404

@app.route('/user/<username>', methods=['DELETE'])
def delete_user_route(username):
	delete_user(username)
	return jsonify('User deleted'), 200

@app.route('/recipe', methods=['POST'])
def submit_recipe_route():
	data = request.get_json()
	recipe.submit_recipe(data['recipe_id'], data['recipe_data'])
	return jsonify('Recipe submitted'), 201

@app.route('/recipe/<recipe_id>', methods=['GET'])
def get_recipe_route(recipe_id):
	recipe_data = recipe.get_recipe(recipe_id)
	if recipe_data:
		return jsonify(recipe_data), 200
	else:
		return jsonify('Recipe not found'), 404

@app.route('/review', methods=['POST'])
def add_review_route():
	data = request.get_json()
	review.add_review(data['user_id'], data['recipe_id'], data['rating'], data['review'])
	return jsonify('Review added'), 201

@app.route('/recommendations/<username>', methods=['GET'])
def get_recommendations_route(username):
	recommendations_data = recommendations.get_recommendations(username)
	if recommendations_data:
		return jsonify(recommendations_data), 200
	else:
		return jsonify('No recommendations available'), 404

if __name__ == '__main__':
	app.run(debug=True)
