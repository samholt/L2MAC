from flask import Flask, request, jsonify, redirect
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import validators
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'super secret key'
login_manager = LoginManager()
login_manager.init_app(app)

# Mock database
url_db = {}
analytics_db = {}
user_db = {}
admin_users = ['admin']

class User(UserMixin):
	def __init__(self, username):
		self.id = username
		self.is_admin = username in admin_users


@login_manager.user_loader
def load_user(username):
	if username in user_db:
		return User(username)


@app.route('/')
def home():
	return 'Hello, World!'


@app.route('/register', methods=['POST'])
def register():
	username = request.json.get('username')
	password = request.json.get('password')
	if not username or not password:
		return jsonify({'error': 'Username and password required'}), 400
	if username in user_db:
		return jsonify({'error': 'Username already exists'}), 400
	user_db[username] = generate_password_hash(password)
	return jsonify({'message': 'User registered successfully'}), 200


@app.route('/login', methods=['POST'])
def login():
	username = request.json.get('username')
	password = request.json.get('password')
	if not username or not password:
		return jsonify({'error': 'Username and password required'}), 400
	if username not in user_db or not check_password_hash(user_db[username], password):
		return jsonify({'error': 'Invalid username or password'}), 400
	login_user(User(username))
	return jsonify({'message': 'Logged in successfully'}), 200


@app.route('/logout')
@login_required
def logout():
	logout_user()
	return jsonify({'message': 'Logged out successfully'}), 200


@app.route('/shorten_url', methods=['POST'])
@login_required
def shorten_url():
	url = request.json.get('url')
	custom_short_url = request.json.get('custom_short_url')
	expiration_date = request.json.get('expiration_date')
	if not validators.url(url):
		return jsonify({'error': 'Invalid URL'}), 400

	short_url = 'short.ly/' + (custom_short_url if custom_short_url and 'short.ly/' + custom_short_url not in url_db else url.split('//')[1].replace('.', ''))
	url_db[short_url] = {'url': url, 'username': current_user.id, 'expiration_date': expiration_date}
	return jsonify({'short_url': short_url})


@app.route('/<path:short_url>', methods=['GET'])
@login_required
def redirect_url(short_url):
	url = url_db.get('short.ly/' + short_url)
	if url is None:
		return jsonify({'error': 'Invalid shortened URL'}), 404

	# Check if URL has expired
	if datetime.now() > datetime.fromisoformat(url['expiration_date']):
		return jsonify({'error': 'URL has expired'}), 404

	# Record analytics
	ip = request.remote_addr
	location = 'Unknown' # Mock location as we cannot use geoip2
	access_time = datetime.now().isoformat()
	analytics_db['short.ly/' + short_url] = {'access_time': access_time, 'location': location}

	return redirect(url['url'], code=302)


@app.route('/view_urls')
@login_required
def view_urls():
	user_urls = {k: v for k, v in url_db.items() if v['username'] == current_user.id}
	return jsonify(user_urls)


@app.route('/edit_url/<path:short_url>', methods=['POST'])
@login_required
def edit_url(short_url):
	new_url = request.json.get('url')
	if not validators.url(new_url):
		return jsonify({'error': 'Invalid URL'}), 400

	url_data = url_db.get('short.ly/' + short_url)
	if url_data is None or url_data['username'] != current_user.id:
		return jsonify({'error': 'Invalid shortened URL or not owned by user'}), 404

	url_db['short.ly/' + short_url] = {'url': new_url, 'username': current_user.id, 'expiration_date': url_data['expiration_date']}
	return jsonify({'message': 'URL updated successfully'})


@app.route('/delete_url/<path:short_url>', methods=['DELETE'])
@login_required
def delete_url(short_url):
	url_data = url_db.get('short.ly/' + short_url)
	if url_data is None or url_data['username'] != current_user.id:
		return jsonify({'error': 'Invalid shortened URL or not owned by user'}), 404

	del url_db['short.ly/' + short_url]
	return jsonify({'message': 'URL deleted successfully'})


@app.route('/admin/view_all_urls')
@login_required
def admin_view_all_urls():
	if not current_user.is_admin:
		return jsonify({'error': 'Unauthorized'}), 403
	return jsonify(url_db)


@app.route('/admin/view_all_users')
@login_required
def admin_view_all_users():
	if not current_user.is_admin:
		return jsonify({'error': 'Unauthorized'}), 403
	return jsonify(list(user_db.keys()))


@app.route('/admin/delete_url/<path:short_url>', methods=['DELETE'])
@login_required
def admin_delete_url(short_url):
	if not current_user.is_admin:
		return jsonify({'error': 'Unauthorized'}), 403
	url_data = url_db.get('short.ly/' + short_url)
	if url_data is None:
		return jsonify({'error': 'Invalid shortened URL'}), 404

	del url_db['short.ly/' + short_url]
	return jsonify({'message': 'URL deleted successfully'})


@app.route('/admin/delete_user/<username>', methods=['DELETE'])
@login_required
def admin_delete_user(username):
	if not current_user.is_admin:
		return jsonify({'error': 'Unauthorized'}), 403
	if username not in user_db:
		return jsonify({'error': 'Invalid username'}), 404

	del user_db[username]
	return jsonify({'message': 'User deleted successfully'})


if __name__ == '__main__':
	app.run(debug=True)
