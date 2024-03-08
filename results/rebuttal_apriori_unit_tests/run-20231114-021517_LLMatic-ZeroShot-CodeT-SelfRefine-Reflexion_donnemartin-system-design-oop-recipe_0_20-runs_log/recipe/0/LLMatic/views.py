from flask import request, jsonify, session
from app import app
from models import User, Review, Rating, Admin
from utils import validate_recipe

@app.route('/')
def home():
	return 'Welcome to the Recipe App'

@app.route('/account', methods=['POST'])
def create_account():
	data = request.get_json()
	user = User(**data)
	user.create_account()
	return jsonify({'message': 'Account created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = User.get_by_username(data['username'])
	if user and user.login(data['password']):
		session['username'] = user.username
		return jsonify({'message': 'Logged in successfully'}), 200
	return jsonify({'message': 'Invalid username or password'}), 400

@app.route('/logout', methods=['POST'])
def logout():
	if 'username' in session:
		user = User.get_by_username(session['username'])
		user.logout()
		session.pop('username', None)
	return jsonify({'message': 'Logged out successfully'}), 200

@app.route('/account', methods=['POST'])
def change_password():
	data = request.get_json()
	user = User.get_by_username(session['username'])
	if user and user.change_password(data['old_password'], data['new_password']):
		return jsonify({'message': 'Password changed successfully'}), 200
	return jsonify({'message': 'Invalid old password'}), 400

@app.route('/profile', methods=['GET'])
def view_profile():
	user = User.get_by_username(session['username'])
	if user:
		return jsonify(user.view_profile()), 200
	return jsonify({'message': 'User not found'}), 404

@app.route('/follow', methods=['POST'])
def follow():
	data = request.get_json()
	user = User.get_by_username(session['username'])
	user.follow(data['user_id'])
	return jsonify({'message': 'Followed user successfully'}), 200

@app.route('/feed', methods=['GET'])
def get_feed():
	user = User.get_by_username(session['username'])
	feed = user.get_feed()
	return jsonify(feed), 200

@app.route('/review', methods=['POST'])
def submit_review():
	data = request.get_json()
	user = User.get_by_username(session['username'])
	review = Review(data['recipe_id'], user, data['text'])
	review.submit_review()
	return jsonify({'message': 'Review submitted successfully'}), 201

@app.route('/rating', methods=['POST'])
def submit_rating():
	data = request.get_json()
	user = User.get_by_username(session['username'])
	rating = Rating(data['recipe_id'], user, data['score'])
	rating.submit_rating()
	return jsonify({'message': 'Rating submitted successfully'}), 201

@app.route('/rating', methods=['GET'])
def get_average_rating():
	recipe_id = request.args.get('recipe_id')
	average_rating = Rating.get_average_rating(recipe_id)
	return jsonify({'average_rating': average_rating}), 200

@app.route('/admin/manage_recipe', methods=['POST'])
def manage_recipe():
	data = request.get_json()
	admin = Admin.get_by_username(session['username'])
	if admin and admin.manage_recipe(data['recipe_id'], data['new_data']):
		return jsonify({'message': 'Recipe updated successfully'}), 200
	return jsonify({'message': 'Failed to update recipe'}), 400

@app.route('/admin/monitor_site_usage', methods=['GET'])
def monitor_site_usage():
	admin = Admin.get_by_username(session['username'])
	if admin:
		stats = admin.monitor_site_usage()
		return jsonify(stats), 200
	return jsonify({'message': 'Failed to get site usage statistics'}), 400

# Rest of the routes remain the same
