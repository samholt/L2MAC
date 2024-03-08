from flask import Flask, request, jsonify
from users import UserManager
from recipes import Recipe
from reviews import Review
from categories import Categories
from admin import Admin
from recommendations import Recommendation

app = Flask(__name__)

user_manager = UserManager()
recipe_manager = Recipe()
review_manager = Review()
category_manager = Categories()
admin_manager = Admin()
recommendation_manager = Recommendation(user_manager, recipe_manager)

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	response = user_manager.create_user(data['id'], data['name'], data['email'])
	return jsonify(response)

@app.route('/user/<id>', methods=['GET', 'PUT', 'DELETE'])
def handle_user(id):
	if request.method == 'GET':
		user = user_manager.get_user(id)
		if user:
			return jsonify(user.__dict__)
		else:
			return jsonify({'error': 'User not found'}), 404
	elif request.method == 'PUT':
		data = request.get_json()
		response = user_manager.update_user(id, data.get('name'), data.get('email'))
		return jsonify(response)
	elif request.method == 'DELETE':
		response = user_manager.delete_user(id)
		return jsonify(response)

@app.route('/recipe', methods=['POST'])
def submit_recipe():
	data = request.get_json()
	response = recipe_manager.submit_recipe(data['id'], data)
	return jsonify(response)

@app.route('/recipe/<id>', methods=['GET', 'PUT', 'DELETE'])
def handle_recipe(id):
	if request.method == 'GET':
		recipe = recipe_manager.get_recipe(id)
		return jsonify(recipe)
	elif request.method == 'PUT':
		data = request.get_json()
		response = recipe_manager.edit_recipe(id, data)
		return jsonify(response)
	elif request.method == 'DELETE':
		response = recipe_manager.delete_recipe(id)
		return jsonify(response)

@app.route('/review', methods=['POST'])
def add_review():
	data = request.get_json()
	response = review_manager.add_review(data['user_id'], data['recipe_id'], data['rating'], data['review'])
	return jsonify(response)

@app.route('/review/<recipe_id>', methods=['GET'])
def get_reviews(recipe_id):
	response = review_manager.get_reviews(recipe_id)
	return jsonify(response)

@app.route('/category', methods=['POST'])
def add_category():
	data = request.get_json()
	category_manager.add_category(data['category_type'], data['category'])
	return jsonify({'status': 'Category added successfully'})

@app.route('/category/<category_type>', methods=['GET'])
def get_categories(category_type):
	categories = category_manager.get_categories(category_type)
	return jsonify(categories)

@app.route('/recommendation/<user_id>', methods=['GET'])
def get_recommendations(user_id):
	recommendations, status_code = recommendation_manager.recommend(user_id)
	return jsonify(recommendations), status_code

if __name__ == '__main__':
	app.run(debug=True)
