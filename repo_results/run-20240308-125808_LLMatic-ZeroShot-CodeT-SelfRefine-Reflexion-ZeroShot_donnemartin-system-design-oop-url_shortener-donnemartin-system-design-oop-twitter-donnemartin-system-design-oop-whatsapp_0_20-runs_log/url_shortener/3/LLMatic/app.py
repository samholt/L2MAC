from flask import Flask, redirect, abort, request
from url_shortener import validate_url, handle_custom_link, set_expiration, get_short_link
from analytics import track_click, get_click_data
from user_accounts import UserAccount
from admin_dashboard import AdminDashboard
from database import url_db

app = Flask(__name__)

user_account = UserAccount()
admin_dashboard = AdminDashboard()

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/<short_url>')
def redirect_to_original(short_url):
	url = get_short_link(short_url)
	if url != 'This URL has expired.':
		track_click(short_url, request.remote_addr)
		return redirect(url_db[short_url])
	else:
		abort(404)

@app.route('/create_short_url', methods=['POST'])
def create_short_url():
	data = request.get_json()
	url = data.get('url')
	custom_link = data.get('custom_link')
	expiration_time = data.get('expiration_time')
	if validate_url(url):
		short_link = handle_custom_link(custom_link)
		set_expiration(short_link, expiration_time)
		url_db[short_link] = url
		return {'short_link': short_link}
	else:
		abort(400, 'Invalid URL')

@app.route('/get_click_data/<short_url>', methods=['GET'])
def get_click_data_route(short_url):
	return {'click_data': get_click_data(short_url)}

@app.route('/create_account', methods=['POST'])
def create_account():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	return {'message': user_account.create_account(username, password)}

@app.route('/view_urls/<username>', methods=['GET'])
def view_urls(username):
	return {'urls': user_account.view_urls(username)}

@app.route('/add_url', methods=['POST'])
def add_url():
	data = request.get_json()
	username = data.get('username')
	url = data.get('url')
	return {'message': user_account.add_url(username, url)}

@app.route('/delete_url', methods=['POST'])
def delete_url():
	data = request.get_json()
	username = data.get('username')
	url = data.get('url')
	return {'message': user_account.delete_url(username, url)}

@app.route('/view_all_urls', methods=['GET'])
def view_all_urls():
	return {'all_urls': admin_dashboard.view_all_urls()}

@app.route('/delete_user', methods=['POST'])
def delete_user():
	data = request.get_json()
	username = data.get('username')
	return {'message': admin_dashboard.delete_user(username)}

@app.route('/view_system_performance', methods=['GET'])
def view_system_performance():
	return {'system_performance': admin_dashboard.view_system_performance()}

if __name__ == '__main__':
	app.run(debug=True)

