from flask import Flask, request, jsonify, redirect
from services.url_shortener import URLShortener
from services.user_service import UserService
from services.admin_service import AdminService

app = Flask(__name__)

url_shortener = URLShortener()
user_service = UserService()
admin_service = AdminService()

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	short_url = url_shortener.shorten(data['url'], data.get('custom_alias'))
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	url = url_shortener.get_url(short_url)
	if url is None:
		return 'URL not found', 404
	return redirect(url, code=302)

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = user_service.create_user(data['username'], data['password'])
	return jsonify(user), 201

@app.route('/user/<username>/urls', methods=['GET'])
def get_user_urls(username):
	urls = user_service.get_user_urls(username)
	return jsonify(urls), 200

@app.route('/admin/urls', methods=['GET'])
def get_all_urls():
	urls = admin_service.get_all_urls()
	return jsonify(urls), 200

if __name__ == '__main__':
	app.run(debug=True)
