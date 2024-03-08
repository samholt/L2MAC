from flask import Flask, request, jsonify
from user import User
from recipe import Recipe
from review import Review
from admin import Admin

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/create_account', methods=['POST'])
def create_account():
	data = request.get_json()
	user = User(data['username'], data['password'])
	user.create_account(data['username'], data['password'])
	return jsonify({'message': 'Account created successfully'}), 201

@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
	data = request.get_json()
	recipe = Recipe(data['ingredients'], data['instructions'], data['images'], data['category'], data['dietary_needs'], data['timestamp'])
	message = recipe.submit_recipe()
	return jsonify({'message': message}), 201

@app.route('/submit_review', methods=['POST'])
def submit_review():
	data = request.get_json()
	review = Review(data['user'], data['recipe'], data['rating'], data['review_text'])
	message = review.submit_review()
	return jsonify({'message': message}), 201

@app.route('/manage_recipes', methods=['DELETE'])
def manage_recipes():
	data = request.get_json()
	admin = Admin(data['username'], data['password'])
	message = admin.manage_recipes(data['recipe'])
	return jsonify({'message': message}), 200

@app.route('/remove_inappropriate_content', methods=['DELETE'])
def remove_inappropriate_content():
	data = request.get_json()
	admin = Admin(data['username'], data['password'])
	message = admin.remove_inappropriate_content(data['review'])
	return jsonify({'message': message}), 200

if __name__ == '__main__':
	app.run(debug=True)
