from flask import Flask, redirect, abort, request, jsonify
from url_shortener import DATABASE, validate_url, generate_short_url, handle_custom_short_link
from analytics import track_click, get_analytics
from user_accounts import create_account, add_url_to_account, remove_url_from_account, get_user_urls, authenticate_user
from admin_dashboard import view_all_urls, delete_url, delete_user, view_system_performance
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
	return jsonify(message='Hello, World!'), 200

@app.route('/<short_url>')
def redirect_to_url(short_url):
	if short_url in DATABASE:
		if datetime.now() <= DATABASE[short_url]['expiry_date']:
			track_click(short_url, request.remote_addr)
			return redirect(DATABASE[short_url]['url'], code=302)
	abort(404)

@app.route('/create_account', methods=['POST'])
def create_new_account():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	result = create_account(username, password)
	return jsonify(result=result), 200 if result else 400

@app.route('/add_url', methods=['POST'])
def add_url():
	data = request.get_json()
	username = data.get('username')
	short_url = data.get('short_url')
	result = add_url_to_account(username, short_url)
	return jsonify(result=result), 200 if result else 400

@app.route('/remove_url', methods=['POST'])
def remove_url():
	data = request.get_json()
	username = data.get('username')
	short_url = data.get('short_url')
	result = remove_url_from_account(username, short_url)
	return jsonify(result=result), 200 if result else 400

@app.route('/get_user_urls', methods=['POST'])
def get_urls():
	data = request.get_json()
	username = data.get('username')
	result = get_user_urls(username)
	return jsonify(result=result), 200 if result else 400

@app.route('/authenticate_user', methods=['POST'])
def authenticate():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	result = authenticate_user(username, password)
	return jsonify(result=result), 200 if result else 400

@app.route('/view_all_urls', methods=['GET'])
def view_urls():
	result = view_all_urls()
	return jsonify(result=result), 200 if result else 400

@app.route('/delete_url', methods=['POST'])
def del_url():
	data = request.get_json()
	short_url = data.get('short_url')
	result = delete_url(short_url)
	return jsonify(result=result), 200 if result else 400

@app.route('/delete_user', methods=['POST'])
def del_user():
	data = request.get_json()
	username = data.get('username')
	result = delete_user(username)
	return jsonify(result=result), 200 if result else 400

@app.route('/view_system_performance', methods=['GET'])
def view_performance():
	result = view_system_performance()
	return jsonify(result=result), 200 if result else 400

if __name__ == '__main__':
	app.run(debug=True)
