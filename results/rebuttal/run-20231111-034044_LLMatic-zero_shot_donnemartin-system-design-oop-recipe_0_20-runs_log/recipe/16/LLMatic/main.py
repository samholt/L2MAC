from flask import Flask, request, jsonify
from user import User
from recipe import Recipe
from review import Review
from category import Category
from admin import Admin
from search import Search
from recommendation import Recommendation
from community import Community

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['username'], data['password'])
	response = user.register()
	return jsonify(response)

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = User(data['username'], data['password'])
	response = user.login()
	return jsonify(response)

@app.route('/logout', methods=['POST'])
def logout():
	data = request.get_json()
	user = User(data['username'], data['password'])
	response = user.logout()
	return jsonify(response)

@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	recipe = Recipe(data)
	response = recipe.create_recipe()
	return jsonify(response)

@app.route('/recipe', methods=['GET'])
def view_recipe():
	data = request.get_json()
	recipe = Recipe(data)
	response = recipe.view_recipe()
	return jsonify(response)

@app.route('/recipe', methods=['PUT'])
def edit_recipe():
	data = request.get_json()
	recipe = Recipe(data)
	response = recipe.edit_recipe()
	return jsonify(response)

@app.route('/recipe', methods=['DELETE'])
def delete_recipe():
	data = request.get_json()
	recipe = Recipe(data)
	response = recipe.delete_recipe()
	return jsonify(response)

@app.route('/review', methods=['POST'])
def create_review():
	data = request.get_json()
	review = Review(data)
	response = review.create_review()
	return jsonify(response)

@app.route('/review', methods=['GET'])
def view_review():
	data = request.get_json()
	review = Review(data)
	response = review.view_review()
	return jsonify(response)

@app.route('/review', methods=['PUT'])
def edit_review():
	data = request.get_json()
	review = Review(data)
	response = review.edit_review()
	return jsonify(response)

@app.route('/review', methods=['DELETE'])
def delete_review():
	data = request.get_json()
	review = Review(data)
	response = review.delete_review()
	return jsonify(response)

@app.route('/category', methods=['POST'])
def create_category():
	data = request.get_json()
	category = Category(data)
	response = category.create_category()
	return jsonify(response)

@app.route('/category', methods=['GET'])
def view_category():
	data = request.get_json()
	category = Category(data)
	response = category.view_category()
	return jsonify(response)

@app.route('/category', methods=['PUT'])
def edit_category():
	data = request.get_json()
	category = Category(data)
	response = category.edit_category()
	return jsonify(response)

@app.route('/category', methods=['DELETE'])
def delete_category():
	data = request.get_json()
	category = Category(data)
	response = category.delete_category()
	return jsonify(response)

@app.route('/admin', methods=['POST'])
def admin_action():
	data = request.get_json()
	admin = Admin(data)
	response = admin.perform_action()
	return jsonify(response)

@app.route('/search', methods=['GET'])
def search():
	data = request.get_json()
	search = Search(data)
	response = search.perform_search()
	return jsonify(response)

@app.route('/recommendation', methods=['GET'])
def recommendation():
	data = request.get_json()
	recommendation = Recommendation(data)
	response = recommendation.get_recommendations()
	return jsonify(response)

@app.route('/community', methods=['POST'])
def community_action():
	data = request.get_json()
	community = Community(data)
	response = community.perform_action()
	return jsonify(response)

if __name__ == '__main__':
	app.run(debug=True)
