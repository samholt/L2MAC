from flask import Flask, request
from user import User
from url import URL
from analytics import get_url_analytics, update_url_analytics
from admin import Admin
from database import Database

app = Flask(__name__)

# Mock database
db = Database()

@app.route('/create_user', methods=['POST'])
def create_user():
	username = request.json.get('username')
	password = request.json.get('password')
	user = User(username, password)
	db.users[username] = user
	return {'message': 'User created successfully'}, 201

@app.route('/edit_user', methods=['PUT'])
def edit_user():
	username = request.json.get('username')
	password = request.json.get('password')
	user = db.users.get(username)
	if user:
		user.edit_user(username, password)
		return {'message': 'User updated successfully'}, 200
	return {'message': 'User not found'}, 404

@app.route('/delete_user', methods=['DELETE'])
def delete_user():
	username = request.json.get('username')
	user = db.users.get(username)
	if user:
		user.delete_user()
		del db.users[username]
		return {'message': 'User deleted successfully'}, 200
	return {'message': 'User not found'}, 404

@app.route('/create_url', methods=['POST'])
def create_url():
	original_url = request.json.get('original_url')
	username = request.json.get('username')
	user = db.users.get(username)
	if user:
		url = URL(original_url, user)
		user.urls.append(url.short_url)
		db.urls[url.short_url] = url
		return {'message': 'URL created successfully', 'short_url': url.short_url}, 201
	return {'message': 'User not found'}, 404

@app.route('/<short_url>', methods=['GET'])
def redirect(short_url):
	url = db.urls.get(short_url)
	if url and not url.is_expired():
		update_url_analytics(url.original_url, request.remote_addr)
		return {'redirect': url.redirect()}, 302
	return {'message': 'URL not found or expired'}, 404

@app.route('/view_analytics', methods=['GET'])
def view_analytics():
	username = request.json.get('username')
	user = db.users.get(username)
	if user:
		return user.view_analytics(), 200
	return {'message': 'User not found'}, 404

@app.route('/admin/view_all_urls', methods=['GET'])
def admin_view_all_urls():
	admin = Admin(db)
	return {'all_urls': [url.short_url for url in admin.view_all_urls()]}, 200

@app.route('/admin/delete_url', methods=['DELETE'])
def admin_delete_url():
	short_url = request.json.get('short_url')
	admin = Admin(db)
	if admin.delete_url(short_url):
		return {'message': 'URL deleted successfully'}, 200
	return {'message': 'URL not found'}, 404

@app.route('/admin/delete_user', methods=['DELETE'])
def admin_delete_user():
	username = request.json.get('username')
	admin = Admin(db)
	if admin.delete_user(username):
		return {'message': 'User deleted successfully'}, 200
	return {'message': 'User not found'}, 404

@app.route('/admin/monitor_system', methods=['GET'])
def admin_monitor_system():
	admin = Admin(db)
	return admin.monitor_system(), 200

if __name__ == '__main__':
	app.run(debug=True)
