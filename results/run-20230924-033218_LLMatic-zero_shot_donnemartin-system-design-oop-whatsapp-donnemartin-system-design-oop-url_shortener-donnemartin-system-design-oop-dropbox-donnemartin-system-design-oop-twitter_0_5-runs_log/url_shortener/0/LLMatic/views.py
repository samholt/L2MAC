from flask import request, redirect, Blueprint
from models import User, URL, Click
from utils import validate_url, generate_shortened_url, gather_click_data
from datetime import datetime


# Mock database
users = []
urls = []
clicks = []


# Create a blueprint
views = Blueprint('views', __name__)


@views.route('/register', methods=['POST'])
def register():
	username = request.form.get('username')
	password = request.form.get('password')
	user = User(id=len(users)+1, username=username, password=password, urls=[])
	users.append(user)
	return 'User registered successfully'


@views.route('/login', methods=['POST'])
def login():
	username = request.form.get('username')
	password = request.form.get('password')
	for user in users:
		if user.username == username and user.password == password:
			return 'User logged in successfully'
	return 'Invalid username or password'


@views.route('/shorten', methods=['POST'])
def shorten_url():
	original_url = request.form.get('original_url')
	custom = request.form.get('custom')
	expiration_date = request.form.get('expiration_date')
	if not validate_url(original_url):
		return 'Invalid URL'
	shortened_url = generate_shortened_url(original_url, custom)
	url = URL(id=len(urls)+1, original_url=original_url, shortened_url=shortened_url, user_id=None, clicks=[], expiration_date=expiration_date)
	urls.append(url)
	return 'URL shortened successfully'


@views.route('/<shortened_url>', methods=['GET'])
def redirect_url(shortened_url):
	for url in urls:
		if url.shortened_url == shortened_url:
			if url.expiration_date and datetime.strptime(url.expiration_date, '%Y-%m-%d') < datetime.now():
				return 'URL expired'
			return redirect(url.original_url)
	return 'URL not found'


@views.route('/edit', methods=['POST'])
def edit_url():
	url_id = request.form.get('url_id')
	new_url = request.form.get('new_url')
	for url in urls:
		if url.id == int(url_id):
			url.original_url = new_url
			return 'URL edited successfully'
	return 'URL not found'


@views.route('/delete', methods=['POST'])
def delete_url():
	url_id = request.form.get('url_id')
	for url in urls:
		if url.id == int(url_id):
			urls.remove(url)
			return 'URL deleted successfully'
	return 'URL not found'


@views.route('/analytics', methods=['GET'])
def view_analytics():
	url_id = request.args.get('url_id')
	for url in urls:
		if url.id == int(url_id):
			return str(url.clicks)
	return 'URL not found'


@views.route('/delete_user', methods=['POST'])
def delete_user():
	user_id = request.form.get('user_id')
	for user in users:
		if user.id == int(user_id):
			users.remove(user)
			return 'User account deleted successfully'
	return 'User not found'


@views.route('/admin', methods=['GET'])
def admin_dashboard():
	if request.args.get('username') == 'admin':
		return {'users': users, 'urls': urls}
	return 'Access denied'

