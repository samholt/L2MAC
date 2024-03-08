from flask import Flask, request, jsonify
from user import User
from recipe import Recipe
from review import Review
from admin import Admin

app = Flask(__name__)

users = {'test': User('test', 'test')}
recipes = {'test recipe': Recipe('test recipe', 'test ingredients', 'test instructions', 'test images', 'test categories')}
admins = {}

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	password = data['password']
	user = User(username, password)
	users[username] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username in users and users[username].password == password:
		return jsonify({'message': 'Login successful'}), 200
	else:
		return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
	data = request.get_json()
	username = data['username']
	recipe_data = data['recipe']
	recipe = Recipe(**recipe_data)
	if users[username].submit_recipe(recipe):
		recipes[recipe.name] = recipe
		return jsonify({'message': 'Recipe submitted successfully'}), 201
	else:
		return jsonify({'message': 'Invalid recipe data'}), 400

@app.route('/edit_recipe', methods=['PUT'])
def edit_recipe():
	data = request.get_json()
	username = data['username']
	recipe_name = data['recipe_name']
	new_recipe_data = data['new_recipe_data']
	if username in users and recipe_name in recipes and users[username].edit_recipe(recipes[recipe_name], **new_recipe_data):
		recipes[recipe_name] = Recipe(**new_recipe_data)
		return jsonify({'message': 'Recipe edited successfully'}), 200
	else:
		return jsonify({'message': 'Invalid recipe data or recipe does not exist'}), 400

@app.route('/delete_recipe', methods=['DELETE'])
def delete_recipe():
	data = request.get_json()
	username = data['username']
	recipe_name = data['recipe_name']
	if username in users and recipe_name in recipes and users[username].delete_recipe(recipes[recipe_name]):
		del recipes[recipe_name]
		return jsonify({'message': 'Recipe deleted successfully'}), 200
	else:
		return jsonify({'message': 'Invalid recipe data or recipe does not exist'}), 400

@app.route('/save_favorite_recipe', methods=['POST'])
def save_favorite_recipe():
	data = request.get_json()
	username = data['username']
	recipe_name = data['recipe_name']
	if recipe_name in recipes:
		users[username].save_favorite_recipe(recipes[recipe_name])
		return jsonify({'message': 'Recipe saved as favorite successfully'}), 200
	else:
		return jsonify({'message': 'Recipe does not exist'}), 400

@app.route('/rate_recipe', methods=['POST'])
def rate_recipe():
	data = request.get_json()
	username = data['username']
	recipe_name = data['recipe_name']
	rating = data['rating']
	review_text = data['review_text']
	if recipe_name in recipes:
		users[username].rate_recipe(recipes[recipe_name], rating, review_text)
		return jsonify({'message': 'Recipe rated successfully'}), 200
	else:
		return jsonify({'message': 'Recipe does not exist'}), 400

@app.route('/follow_user', methods=['POST'])
def follow_user():
	data = request.get_json()
	username = data['username']
	user_to_follow = data['user_to_follow']
	if user_to_follow in users:
		users[username].follow_user(users[user_to_follow])
		return jsonify({'message': 'User followed successfully'}), 200
	else:
		return jsonify({'message': 'User does not exist'}), 400

@app.route('/unfollow_user', methods=['POST'])
def unfollow_user():
	data = request.get_json()
	username = data['username']
	user_to_unfollow = data['user_to_unfollow']
	if user_to_unfollow in users:
		users[username].unfollow_user(users[user_to_unfollow])
		return jsonify({'message': 'User unfollowed successfully'}), 200
	else:
		return jsonify({'message': 'User does not exist'}), 400

@app.route('/update_feed', methods=['GET'])
def update_feed():
	username = request.args.get('username')
	users[username].update_feed()
	return jsonify({'message': 'Feed updated successfully'}), 200

@app.route('/share_recipe', methods=['POST'])
def share_recipe():
	data = request.get_json()
	username = data['username']
	recipe_name = data['recipe_name']
	platform = data['platform']
	if recipe_name in recipes:
		message = users[username].share_recipe(recipes[recipe_name], platform)
		return jsonify({'message': message}), 200
	else:
		return jsonify({'message': 'Recipe does not exist'}), 400

@app.route('/get_recommendations', methods=['GET'])
def get_recommendations():
	username = request.args.get('username')
	recommendations = users[username].get_recommendations(list(recipes.values()))
	return jsonify({'recommendations': [recipe.name for recipe in recommendations]}), 200

@app.route('/receive_notifications', methods=['GET'])
def receive_notifications():
	username = request.args.get('username')
	new_recipes = list(recipes.values())
	users[username].receive_notifications(new_recipes)
	return jsonify({'notifications': users[username].notifications}), 200

@app.route('/manage_recipe', methods=['POST'])
def manage_recipe():
	data = request.get_json()
	admin_username = data['admin_username']
	recipe_name = data['recipe_name']
	if recipe_name in recipes:
		admins[admin_username].manage_recipe(recipes[recipe_name])
		return jsonify({'message': 'Recipe managed successfully'}), 200
	else:
		return jsonify({'message': 'Recipe does not exist'}), 400

@app.route('/remove_content', methods=['DELETE'])
def remove_content():
	data = request.get_json()
	admin_username = data['admin_username']
	content = data['content']
	admins[admin_username].remove_content(content)
	return jsonify({'message': 'Content removed successfully'}), 200

@app.route('/monitor_site_usage', methods=['POST'])
def monitor_site_usage():
	data = request.get_json()
	admin_username = data['admin_username']
	usage_statistics = data['usage_statistics']
	admins[admin_username].monitor_site_usage(usage_statistics)
	return jsonify({'message': 'Site usage monitored successfully'}), 200

@app.route('/monitor_user_engagement', methods=['POST'])
def monitor_user_engagement():
	data = request.get_json()
	admin_username = data['admin_username']
	user_engagement = data['user_engagement']
	admins[admin_username].monitor_user_engagement(user_engagement)
	return jsonify({'message': 'User engagement monitored successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
