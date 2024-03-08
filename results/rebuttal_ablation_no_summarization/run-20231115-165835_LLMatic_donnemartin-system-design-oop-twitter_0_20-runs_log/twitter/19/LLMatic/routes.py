from flask import Blueprint, request
from services import register_user, authenticate_user, edit_profile, toggle_privacy, create_post, delete_post, search_posts

routes = Blueprint('routes', __name__)

@routes.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	result = register_user(data['email'], data['username'], data['password'])
	return {'success': result}, 200 if result else 400

@routes.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	result = authenticate_user(data['email'], data['password'])
	return {'success': result}, 200 if result else 400

@routes.route('/edit-profile', methods=['POST'])
def edit_profile_route():
	data = request.get_json()
	result = edit_profile(data['email'], data['profile_picture'], data['bio'], data['website_link'], data['location'])
	return {'success': result}, 200 if result else 400

@routes.route('/toggle-privacy', methods=['POST'])
def toggle_privacy_route():
	data = request.get_json()
	result = toggle_privacy(data['email'])
	return {'success': result}, 200 if result else 400

@routes.route('/create-post', methods=['POST'])
def create_post_route():
	data = request.get_json()
	result = create_post(data['email'], data['text_content'], data['images'])
	return {'success': result}, 200 if result else 400

@routes.route('/delete-post', methods=['POST'])
def delete_post_route():
	data = request.get_json()
	result = delete_post(data['post_id'])
	return {'success': result}, 200 if result else 400

@routes.route('/search-posts', methods=['GET'])
def search_posts_route():
	query = request.args.get('query')
	result = search_posts(query)
	return {'posts': result}, 200 if result else 400
