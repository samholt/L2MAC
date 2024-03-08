from flask import Flask, request, jsonify, redirect, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import hashlib
import re
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'super secret key'
login_manager = LoginManager()
login_manager.init_app(app)

URL_DB = {}
ANALYTICS_DB = {}
USER_DB = {}

try:
	from geoip2.database import Reader
	GEOIP2_AVAILABLE = True
except ImportError:
	GEOIP2_AVAILABLE = False

@login_manager.user_loader
def load_user(user_id):
	return USER_DB.get(user_id)

class User(UserMixin):
	def __init__(self, id, password, is_admin=False):
		self.id = id
		self.password = password
		self.is_admin = is_admin

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
	username = request.json.get('username')
	password = request.json.get('password')
	is_admin = request.json.get('is_admin', False)
	if not username or not password:
		return jsonify({'error': 'Username and password required'}), 400
	if username in USER_DB:
		return jsonify({'error': 'Username already exists'}), 400
	user = User(username, hashlib.md5(password.encode()).hexdigest(), is_admin)
	USER_DB[username] = user
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	username = request.json.get('username')
	password = request.json.get('password')
	if not username or not password:
		return jsonify({'error': 'Username and password required'}), 400
	user = USER_DB.get(username)
	if user is None or user.password != hashlib.md5(password.encode()).hexdigest():
		return jsonify({'error': 'Invalid username or password'}), 400
	login_user(user)
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return jsonify({'message': 'Logged out successfully'}), 200

@app.route('/shorten', methods=['POST'])
@login_required
def shorten_url():
	url = request.json.get('url')
	expiration_date = request.json.get('expiration_date')
	custom_short_url = request.json.get('custom_short_url')
	if not re.match('^(http|https)://', url):
		return jsonify({'error': 'Invalid URL'}), 400
	if custom_short_url and custom_short_url in URL_DB:
		return jsonify({'error': 'Custom short URL already in use'}), 400
	short_url = custom_short_url if custom_short_url else hashlib.md5(url.encode()).hexdigest()[:10]
	URL_DB[short_url] = {'url': url, 'owner': current_user.id, 'expiration_date': expiration_date}
	return jsonify({'short_url': short_url})

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url_data = URL_DB.get(short_url)
	if url_data is None:
		return jsonify({'error': 'URL not found'}), 404
	if datetime.now() > datetime.strptime(url_data['expiration_date'], '%Y-%m-%d %H:%M:%S'):
		return jsonify({'error': 'URL expired'}), 404
	ip = request.remote_addr
	location = 'Unknown'
	if GEOIP2_AVAILABLE:
		reader = Reader('GeoLite2-City.mmdb')
		response = reader.city(ip)
		location = response.city.name
	ANALYTICS_DB[short_url] = {'access_time': datetime.now(), 'location': location}
	return redirect(url_data['url'], code=302)

@app.route('/<short_url>', methods=['PUT'])
@login_required
def edit_url(short_url):
	url_data = URL_DB.get(short_url)
	if url_data is None:
		return jsonify({'error': 'URL not found'}), 404
	if url_data['owner'] != current_user.id:
		return jsonify({'error': 'Not authorized'}), 403
	new_url = request.json.get('url')
	if not re.match('^(http|https)://', new_url):
		return jsonify({'error': 'Invalid URL'}), 400
	url_data['url'] = new_url
	return jsonify({'message': 'URL updated successfully'})

@app.route('/<short_url>', methods=['DELETE'])
@login_required
def delete_url(short_url):
	url_data = URL_DB.get(short_url)
	if url_data is None:
		return jsonify({'error': 'URL not found'}), 404
	if url_data['owner'] != current_user.id:
		return jsonify({'error': 'Not authorized'}), 403
	del URL_DB[short_url]
	return jsonify({'message': 'URL deleted successfully'})

@app.route('/admin', methods=['GET', 'DELETE'])
@login_required
def admin_dashboard():
	if not current_user.is_admin:
		return jsonify({'error': 'Not authorized'}), 403
	if request.method == 'GET':
		return jsonify({'users': list(USER_DB.keys()), 'urls': URL_DB})
	elif request.method == 'DELETE':
		username = request.json.get('username')
		short_url = request.json.get('short_url')
		if username and username in USER_DB:
			del USER_DB[username]
		if short_url and short_url in URL_DB:
			del URL_DB[short_url]
		return jsonify({'message': 'Deleted successfully'})

if __name__ == '__main__':
	app.run(debug=True)
