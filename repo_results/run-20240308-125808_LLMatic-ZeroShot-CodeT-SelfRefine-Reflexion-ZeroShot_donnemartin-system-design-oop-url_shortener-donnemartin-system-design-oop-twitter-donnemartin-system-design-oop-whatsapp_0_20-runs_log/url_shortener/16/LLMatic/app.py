from flask import Flask, redirect, abort, request
from url_shortener import get_original_url, generate_short_url, url_db
from user import User
from analytics import get_url_stats

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/<short_url>')
def redirect_to_original(short_url):
	url = get_original_url(short_url)
	if url is not None:
		return redirect(url)
	else:
		abort(404)

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	short_url = generate_short_url(data['url'], data.get('custom_alias', None), data.get('expiration', None))
	return {'short_url': short_url}

@app.route('/user', methods=['POST', 'PUT', 'DELETE'])
def manage_user():
	data = request.get_json()
	if request.method == 'POST':
		user = User(data['username'], data['password'])
		return {'status': 'User created', 'user': user.__dict__}
	elif request.method == 'PUT':
		user = next((user for user in User.users if user.username == data['username']), None)
		if user is not None:
			user.edit_user(data['new_username'], data['new_password'])
			return {'status': 'User updated', 'user': user.__dict__}
		else:
			abort(404)
	elif request.method == 'DELETE':
		user = next((user for user in User.users if user.username == data['username']), None)
		if user is not None:
			user.delete_user()
			return {'status': 'User deleted'}
		else:
			abort(404)

@app.route('/admin', methods=['GET', 'DELETE'])
def admin_dashboard():
	if request.method == 'GET':
		return {'users': [user.__dict__ for user in User.users], 'urls': url_db}
	elif request.method == 'DELETE':
		data = request.get_json()
		if 'user' in data:
			User.users = [user for user in User.users if user.username != data['user']]
		if 'url' in data:
			url_db.pop(data['url'], None)
		return {'status': 'success'}

@app.route('/admin/analytics/<short_url>')
def admin_analytics(short_url):
	return get_url_stats(short_url)

if __name__ == '__main__':
	app.run(debug=True)
