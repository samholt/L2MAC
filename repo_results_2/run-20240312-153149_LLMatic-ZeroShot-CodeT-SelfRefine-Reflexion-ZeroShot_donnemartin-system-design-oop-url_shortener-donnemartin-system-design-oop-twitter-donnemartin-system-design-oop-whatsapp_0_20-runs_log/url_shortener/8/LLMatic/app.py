from flask import Flask, redirect, request
from url_shortener import URLShortener
from user import User
from admin import Admin


url_shortener = URLShortener()
admin = Admin(url_shortener)


def create_app():
	# Create Flask application
	app = Flask(__name__)

	@app.route('/<short_url>')
	def redirect_to_url(short_url):
		# Redirect to the original URL associated with the short URL
		url = url_shortener.get_long_url(short_url)
		if url:
			return redirect(url)
		return 'URL not found', 404

	@app.route('/shorten_url', methods=['POST'])
	def shorten_url():
		# Shorten the provided URL and return the short URL
		original_url = request.json['original_url']
		short_url = url_shortener.shorten_url(original_url)
		return {'short_url': short_url}

	@app.route('/user/create', methods=['POST'])
	def create_user():
		# Create a new user
		username = request.json['username']
		password = request.json['password']
		user = User(username, password)
		user.create_account(url_shortener)
		return {'message': 'User created successfully'}

	@app.route('/user/add_url', methods=['POST'])
	def add_url():
		# Add a new URL for the user
		username = request.json['username']
		long_url = request.json['long_url']
		user = url_shortener.users.get(username)
		if user:
			short_url = user.add_url(long_url, url_shortener)
			return {'short_url': short_url}
		return {'message': 'User not found'}, 404

	@app.route('/user/view_urls', methods=['GET'])
	def view_urls():
		# View all URLs of the user
		username = request.args.get('username')
		user = url_shortener.users.get(username)
		if user:
			return user.view_urls()
		return {'message': 'User not found'}, 404

	@app.route('/user/edit_url', methods=['PUT'])
	def edit_url():
		# Edit a URL of the user
		username = request.json['username']
		short_url = request.json['short_url']
		new_long_url = request.json['new_long_url']
		user = url_shortener.users.get(username)
		if user:
			user.edit_url(short_url, new_long_url, url_shortener)
			return {'message': 'URL edited successfully'}
		return {'message': 'User not found'}, 404

	@app.route('/user/delete_url', methods=['DELETE'])
	def delete_url():
		# Delete a URL of the user
		username = request.json['username']
		short_url = request.json['short_url']
		user = url_shortener.users.get(username)
		if user:
			user.delete_url(short_url, url_shortener)
			return {'message': 'URL deleted successfully'}
		return {'message': 'User not found'}, 404

	@app.route('/user/view_analytics', methods=['GET'])
	def view_analytics():
		# View analytics of a URL of the user
		username = request.args.get('username')
		short_url = request.args.get('short_url')
		user = url_shortener.users.get(username)
		if user:
			return user.view_analytics(short_url, url_shortener)
		return {'message': 'User not found'}, 404

	@app.route('/admin/view_all_urls', methods=['GET'])
	def view_all_urls():
		# View all URLs in the system
		return admin.view_all_urls()

	@app.route('/admin/delete_url', methods=['DELETE'])
	def admin_delete_url():
		# Delete a URL from the system
		short_url = request.json['short_url']
		admin.delete_url(short_url)
		return {'message': 'URL deleted successfully'}

	@app.route('/admin/delete_user', methods=['DELETE'])
	def delete_user():
		# Delete a user from the system
		username = request.json['username']
		admin.delete_user(username)
		return {'message': 'User deleted successfully'}

	@app.route('/admin/monitor_system', methods=['GET'])
	def monitor_system():
		# Monitor the system
		return admin.monitor_system()

	return app


if __name__ == '__main__':
	app = create_app()
	app.run(port=5000)
