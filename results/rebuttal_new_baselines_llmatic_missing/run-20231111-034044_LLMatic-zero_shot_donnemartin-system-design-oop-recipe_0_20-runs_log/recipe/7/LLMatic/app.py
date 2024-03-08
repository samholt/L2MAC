from flask import Flask, request, jsonify
from user import User
from recipe import Recipe
from search import Search
from review import Review
from community import Community
from admin import Admin
from recommendation import Recommendation

app = Flask(__name__)

# Mock database
users_db = {}
recipes_db = {}
reviews_db = {}
community_db = Community()
admin_db = Admin()
recommendation_db = Recommendation()

@app.route('/')
def home():
	return 'Hello, World!', 200

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	if username in users_db:
		return jsonify({'message': 'User already exists'}), 400
	user = User(username, password)
	users_db[username] = user
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	user = users_db.get(username)
	if not user or user.password != password:
		return jsonify({'message': 'Invalid username or password'}), 400
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
	data = request.get_json()
	name = data.get('name')
	ingredients = data.get('ingredients')
	instructions = data.get('instructions')
	images = data.get('images')
	category = data.get('category')
	recipe = Recipe(name, ingredients, instructions, images, category)
	if recipe.submit_recipe():
		recipes_db[name] = recipe
		return jsonify({'message': 'Recipe submitted successfully'}), 200
	return jsonify({'message': 'Failed to submit recipe'}), 400

@app.route('/edit_recipe/<name>', methods=['PUT'])
def edit_recipe(name):
	data = request.get_json()
	recipe = recipes_db.get(name)
	if not recipe:
		return jsonify({'message': 'Recipe not found'}), 404
	new_name = data.get('name')
	new_ingredients = data.get('ingredients')
	new_instructions = data.get('instructions')
	new_images = data.get('images')
	new_category = data.get('category')
	recipe.edit_recipe(new_name, new_ingredients, new_instructions, new_images, new_category)
	del recipes_db[name]
	recipes_db[new_name] = recipe
	return jsonify({'message': 'Recipe edited successfully'}), 200

@app.route('/delete_recipe/<name>', methods=['DELETE'])
def delete_recipe(name):
	recipe = recipes_db.get(name)
	if not recipe:
		return jsonify({'message': 'Recipe not found'}), 404
	recipe.delete_recipe()
	del recipes_db[name]
	return jsonify({'message': 'Recipe deleted successfully'}), 200

@app.route('/search', methods=['GET'])
def search():
	name = request.args.get('name')
	category = request.args.get('category')
	search = Search(list(recipes_db.values()))
	if name:
		results = search.search_by_name(name)
	elif category:
		results = search.search_by_category(category)
	else:
		return jsonify({'message': 'Invalid search parameters'}), 400
	return jsonify({'results': [recipe.name for recipe in results]}), 200

@app.route('/submit_review', methods=['POST'])
def submit_review():
	data = request.get_json()
	username = data.get('username')
	recipe_name = data.get('recipe_name')
	rating = data.get('rating')
	review_text = data.get('review_text')
	user = users_db.get(username)
	recipe = recipes_db.get(recipe_name)
	if not user or not recipe:
		return jsonify({'message': 'User or recipe not found'}), 404
	review = Review(user, recipe, rating, review_text)
	reviews_db[(username, recipe_name)] = review
	return jsonify({'message': 'Review submitted successfully'}), 200

@app.route('/follow', methods=['POST'])
def follow():
	data = request.get_json()
	user_id = data.get('user_id')
	follow_id = data.get('follow_id')
	community_db.follow(user_id, follow_id)
	return jsonify({'message': 'Followed successfully'}), 200

@app.route('/generate_feed/<user_id>', methods=['GET'])
def generate_feed(user_id):
	feed = community_db.generate_feed(user_id)
	return jsonify({'feed': feed}), 200

@app.route('/share_recipe', methods=['POST'])
def share_recipe():
	data = request.get_json()
	user_id = data.get('user_id')
	recipe_id = data.get('recipe_id')
	platform = data.get('platform')
	message = community_db.share_recipe(user_id, recipe_id, platform)
	return jsonify({'message': message}), 200

@app.route('/manage_recipes/<recipe_id>', methods=['POST'])
def manage_recipes(recipe_id):
	data = request.get_json()
	action = data.get('action')
	message = admin_db.manage_recipes(recipe_id, action)
	return jsonify({'message': message}), 200

@app.route('/manage_users/<user_id>', methods=['POST'])
def manage_users(user_id):
	data = request.get_json()
	action = data.get('action')
	message = admin_db.manage_users(user_id, action)
	return jsonify({'message': message}), 200

@app.route('/monitor_site_usage', methods=['GET'])
def monitor_site_usage():
	usage = admin_db.monitor_site_usage()
	return jsonify({'usage': usage}), 200

@app.route('/generate_recommendations/<username>', methods=['GET'])
def generate_recommendations(username):
	recommendations = recommendation_db.generate_recommendations(username)
	return jsonify({'recommendations': [recipe.name for recipe in recommendations]}), 200

if __name__ == '__main__':
	app.run(debug=True)
