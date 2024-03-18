from flask import Flask, request, jsonify, redirect
from shortener import Shortener
from analytics import Analytics
from user import User
from admin import Admin

shortener = Shortener()
analytics = Analytics()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	return 'Hello, World!', 200

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	short_url = shortener.shorten_url(data['url'])
	return jsonify({'short_url': short_url}), 200

@app.route('/<string:short_url>', methods=['GET'])
def redirect_url(short_url):
	original_url = shortener.get_original_url(short_url)
	if original_url:
		return redirect(original_url, code=302)
	else:
		return 'URL not found', 404

@app.route('/analytics', methods=['GET'])
def get_analytics():
	data = analytics.get_clicks()
	return jsonify(data), 200

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(data['username'])
	user.create_account()
	return jsonify({'message': 'User created successfully'}), 200

@app.route('/admin', methods=['POST'])
def create_admin():
	data = request.get_json()
	admin = Admin(data['username'], shortener)
	admin.create_account()
	return jsonify({'message': 'Admin created successfully'}), 200

@app.route('/admin/urls', methods=['GET', 'DELETE'])
def manage_urls():
	admin = Admin('admin', shortener)
	if request.method == 'GET':
		all_urls = admin.view_all_urls()
		return jsonify(all_urls), 200
	elif request.method == 'DELETE':
		data = request.get_json()
		admin.delete_url(data['short_url'])
		return jsonify({'message': 'URL deleted'}), 200

@app.route('/admin/users/<username>', methods=['DELETE'])
def delete_user(username):
	admin = Admin('admin', shortener)
	admin.delete_user(username)
	return jsonify({'message': 'User deleted'}), 200

if __name__ == '__main__':
	app.run(port=5001)
