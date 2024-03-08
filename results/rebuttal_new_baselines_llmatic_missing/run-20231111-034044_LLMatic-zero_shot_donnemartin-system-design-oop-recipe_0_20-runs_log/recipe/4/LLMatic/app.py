from flask import Flask, request, jsonify
from recipes import Recipe
from users import UserManager
from reviews import Review
from categories import Category
from admin import Admin
from recommendations import generate_recommendations

app = Flask(__name__)

recipes = Recipe()
users = UserManager()
reviews = Review()
categories = Category()
admin = Admin()

@app.route('/recipes', methods=['GET', 'POST'])
def handle_recipes():
	if request.method == 'POST':
		return jsonify(recipes.submit_recipe(request.json['id'], request.json['recipe']))
	else:
		return jsonify(recipes.get_recipe(request.json['id']))

@app.route('/users', methods=['GET', 'POST'])
def handle_users():
	if request.method == 'POST':
		return jsonify(users.create_user(request.json['id'], request.json['name'], request.json['email']))
	else:
		return jsonify(users.get_user(request.json['id']))

@app.route('/reviews', methods=['GET', 'POST'])
def handle_reviews():
	if request.method == 'POST':
		return jsonify(reviews.add_review(request.json['user_id'], request.json['recipe_id'], request.json['rating'], request.json['review']))
	else:
		return jsonify(reviews.get_reviews(request.json['recipe_id']))

@app.route('/categories', methods=['GET', 'POST'])
def handle_categories():
	if request.method == 'POST':
		return jsonify(categories.add_category(request.json['type'], request.json['name']))
	else:
		return jsonify(categories.get_categories(request.json['type']))

@app.route('/admin', methods=['GET', 'POST'])
def handle_admin():
	if request.method == 'POST':
		return jsonify(admin.manage_recipes(request.json['recipe_id'], request.json['action']))
	else:
		return jsonify(admin.remove_inappropriate_content(request.json['user_id']))

@app.route('/recommendations', methods=['GET'])
def handle_recommendations():
	return jsonify(generate_recommendations(request.json['user_id']))

if __name__ == '__main__':
	app.run(debug=True)
