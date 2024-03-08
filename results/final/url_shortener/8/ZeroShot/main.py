from flask import Flask, request, jsonify, redirect
from url_shortener import URLShortener
from user import User
from admin import Admin

app = Flask(__name__)
url_shortener = URLShortener()
users = {}
admins = {}

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	url = data.get('url')
	custom_alias = data.get('custom_alias')
	user_id = data.get('user_id')
	expiration_date = data.get('expiration_date')
	short_url = url_shortener.shorten_url(url, custom_alias, user_id, expiration_date)
	return jsonify({'short_url': short_url})

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	url = url_shortener.get_original_url(short_url)
	if url:
		return redirect(url)
	else:
		return 'URL not found or expired', 404

@app.route('/user/register', methods=['POST'])
def register_user():
	data = request.get_json()
	user_id = data.get('user_id')
	user = User(user_id)
	users[user_id] = user
	return 'User registered successfully'

@app.route('/user/<user_id>/urls', methods=['GET'])
def get_user_urls(user_id):
	user = users.get(user_id)
	if user:
		return jsonify(user.get_urls())
	else:
		return 'User not found', 404

@app.route('/admin/register', methods=['POST'])
def register_admin():
	data = request.get_json()
	admin_id = data.get('admin_id')
	admin = Admin(admin_id)
	admins[admin_id] = admin
	return 'Admin registered successfully'

@app.route('/admin/<admin_id>/urls', methods=['GET'])
def get_all_urls(admin_id):
	admin = admins.get(admin_id)
	if admin:
		return jsonify(url_shortener.get_all_urls())
	else:
		return 'Admin not found', 404

if __name__ == '__main__':
	app.run(debug=True)
