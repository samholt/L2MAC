from flask import Flask, request, jsonify
from user import User, Profile
from recipe import Recipe
from review import Review
from admin import Admin

app = Flask(__name__)

users = {}
recipes = {}
reviews = {}
admins = {}

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(data['username'], data['password'])
	users[data['username']] = user
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
	user = users.get(username)
	if user:
		return jsonify({'username': user.username, 'password': user.password}), 200
	else:
		return jsonify({'message': 'User not found'}), 404

@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	recipe = Recipe(data['name'], data['ingredients'], data['instructions'], data['images'], data['category'])
	recipes[data['name']] = recipe
	return jsonify({'message': 'Recipe created successfully'}), 201

@app.route('/recipe/<name>', methods=['GET'])
def get_recipe(name):
	recipe = recipes.get(name)
	if recipe:
		return jsonify(recipe.to_dict()), 200
	else:
		return jsonify({'message': 'Recipe not found'}), 404

@app.route('/review', methods=['POST'])
def create_review():
	data = request.get_json()
	review = Review(data['user'], data['recipe'], data['rating'], data['review_text'])
	reviews[data['user']] = review
	return jsonify({'message': 'Review created successfully'}), 201

@app.route('/review/<user>', methods=['GET'])
def get_review(user):
	review = reviews.get(user)
	if review:
		return jsonify(review.to_dict()), 200
	else:
		return jsonify({'message': 'Review not found'}), 404

@app.route('/admin', methods=['POST'])
def create_admin():
	data = request.get_json()
	admin = Admin(data['username'], data['password'])
	admins[data['username']] = admin
	return jsonify({'message': 'Admin created successfully'}), 201

@app.route('/admin/<username>', methods=['GET'])
def get_admin(username):
	admin = admins.get(username)
	if admin:
		return jsonify({'username': admin.username, 'password': admin.password}), 200
	else:
		return jsonify({'message': 'Admin not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
