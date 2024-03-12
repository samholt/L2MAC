from flask import Flask, redirect, request, jsonify
from shortener import Shortener
from analytics import Analytics
from user import User
from admin import Admin

shortener = Shortener()
analytics = Analytics()
users = {}
admin = Admin('admin')

app = Flask(__name__)
app.config['shortener'] = shortener
app.config['analytics'] = analytics
app.config['users'] = users
app.config['admin'] = admin

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/shorten', methods=['POST'])
def shorten_url():
	original_url = request.json.get('original_url')
	short_url = app.config['shortener'].shorten_url(original_url)
	return jsonify({'short_url': short_url})

@app.route('/<short_url>')
def redirect_to_original(short_url):
	original_url = app.config['shortener'].get_url(short_url)
	if original_url:
		return redirect(original_url)
	else:
		return 'URL not found', 404

@app.route('/user/create', methods=['POST'])
def create_user():
	username = request.json.get('username')
	user = User(username)
	app.config['users'][username] = user
	return jsonify(user.create_account())

@app.route('/user/<username>/urls', methods=['GET', 'POST', 'PUT', 'DELETE'])
def manage_urls(username):
	user = app.config['users'].get(username)
	if not user:
		return 'User not found', 404
	if request.method == 'GET':
		return jsonify(user.view_urls())
	elif request.method == 'POST':
		short_url = request.json.get('short_url')
		original_url = request.json.get('original_url')
		return jsonify(user.add_url(short_url, original_url))
	elif request.method == 'PUT':
		short_url = request.json.get('short_url')
		new_url = request.json.get('new_url')
		return jsonify(user.edit_url(short_url, new_url))
	elif request.method == 'DELETE':
		short_url = request.json.get('short_url')
		return jsonify(user.delete_url(short_url))

@app.route('/user/<username>/analytics', methods=['GET'])
def view_analytics(username):
	user = app.config['users'].get(username)
	if not user:
		return 'User not found', 404
	return jsonify(user.view_analytics(app.config['analytics']))

@app.route('/admin/urls', methods=['GET', 'DELETE'])
def admin_urls():
	if request.method == 'GET':
		return jsonify(app.config['admin'].view_all_urls())
	elif request.method == 'DELETE':
		short_url = request.json.get('short_url')
		app.config['admin'].delete_url(short_url)
		return 'URL deleted', 200

@app.route('/admin/users', methods=['GET', 'DELETE'])
def admin_users():
	if request.method == 'GET':
		return jsonify({username: user.create_account() for username, user in app.config['users'].items()})
	elif request.method == 'DELETE':
		username = request.json.get('username')
		app.config['admin'].delete_user(username)
		return 'User deleted', 200

@app.route('/admin/analytics', methods=['GET'])
def admin_analytics():
	return jsonify(app.config['admin'].monitor_system(app.config['analytics']))

if __name__ == '__main__':
	app.run(debug=True)
