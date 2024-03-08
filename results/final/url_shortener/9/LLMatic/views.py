from flask import Blueprint, request, jsonify, redirect
from services import validate_and_shorten_url, get_original_url, record_click, create_user, authenticate_user, get_user_urls, get_all_urls, delete_url, get_all_users, delete_user

url_shortener_blueprint = Blueprint('url_shortener', __name__)

@url_shortener_blueprint.route('/', methods=['GET'])
def home():
	return 'Welcome to the URL Shortener Service!'

@url_shortener_blueprint.route('/shorten', methods=['POST'])
def shorten_url():
	original_url = request.json.get('url')
	user = request.json.get('user')
	short_url = validate_and_shorten_url(original_url, user)
	return jsonify({'short_url': short_url})

@url_shortener_blueprint.route('/<short_url>', methods=['GET'])
def redirect_to_original(short_url):
	original_url = get_original_url(short_url)
	if original_url:
		return redirect(original_url)
	else:
		return 'URL not found', 404

@url_shortener_blueprint.route('/<short_url>/stats', methods=['GET'])
def get_click_stats(short_url):
	location = request.headers.get('X-Forwarded-For', request.remote_addr)
	click_count = record_click(short_url, location)
	return jsonify({'click_count': click_count})

@url_shortener_blueprint.route('/register', methods=['POST'])
def register():
	username = request.json.get('username')
	password = request.json.get('password')
	message = create_user(username, password)
	return jsonify({'message': message})

@url_shortener_blueprint.route('/login', methods=['POST'])
def login():
	username = request.json.get('username')
	password = request.json.get('password')
	is_authenticated = authenticate_user(username, password)
	return jsonify({'authenticated': is_authenticated})

@url_shortener_blueprint.route('/user/urls', methods=['GET'])
def get_urls():
	username = request.json.get('username')
	urls = get_user_urls(username)
	return jsonify(urls)

@url_shortener_blueprint.route('/admin/urls', methods=['GET'])
def admin_get_urls():
	urls = get_all_urls()
	return jsonify(urls)

@url_shortener_blueprint.route('/admin/urls/<short_url>', methods=['DELETE'])
def admin_delete_url(short_url):
	message = delete_url(short_url)
	return jsonify({'message': message})

@url_shortener_blueprint.route('/admin/users', methods=['GET'])
def admin_get_users():
	users = get_all_users()
	return jsonify(users)

@url_shortener_blueprint.route('/admin/users/<username>', methods=['DELETE'])
def admin_delete_user(username):
	message = delete_user(username)
	return jsonify({'message': message})
