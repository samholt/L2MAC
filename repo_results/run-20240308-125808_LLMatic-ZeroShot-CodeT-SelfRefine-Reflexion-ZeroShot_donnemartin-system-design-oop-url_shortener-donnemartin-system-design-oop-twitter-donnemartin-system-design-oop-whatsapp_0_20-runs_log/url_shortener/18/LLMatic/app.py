from flask import Flask, redirect, abort, request, jsonify
from url_shortener import get_original_url, generate_short_url, custom_short_link, set_expiration_time, DATABASE as url_db
from analytics import track_click, get_click_data
from user_accounts import UserAccount
from admin_dashboard import view_all_urls, delete_url, delete_user, monitor_system

app = Flask(__name__)

user_accounts = UserAccount()

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/<short_url>')
def redirect_to_original(short_url):
	original_url = get_original_url(short_url)
	if original_url is None or 'Error' in original_url:
		abort(404)
	ip_address = request.remote_addr
	track_click(short_url, ip_address)
	return redirect(original_url, code=302)

@app.route('/shorten', methods=['POST'])
def shorten_url():
	url = request.form.get('url')
	short_url = generate_short_url(url)
	return jsonify({'short_url': short_url})

@app.route('/custom', methods=['POST'])
def custom_url():
	url = request.form.get('url')
	custom_link = request.form.get('custom_link')
	result = custom_short_link(url, custom_link)
	return jsonify({'result': result})

@app.route('/set_expiration', methods=['POST'])
def set_expiration():
	short_url = request.form.get('short_url')
	days = int(request.form.get('days'))
	expiration_time = set_expiration_time(short_url, days)
	return jsonify({'expiration_time': str(expiration_time)})

@app.route('/analytics/<short_url>')
def analytics(short_url):
	data = get_click_data(short_url)
	return jsonify(data)

@app.route('/create_account', methods=['POST'])
def create_account():
	username = request.form.get('username')
	password = request.form.get('password')
	message = user_accounts.create_account(username, password)
	return jsonify({'message': message})

@app.route('/view_urls/<username>')
def view_urls(username):
	urls = user_accounts.view_urls(username)
	return jsonify({'urls': urls})

@app.route('/add_url', methods=['POST'])
def add_url():
	username = request.form.get('username')
	url = request.form.get('url')
	message = user_accounts.add_url(username, url)
	return jsonify({'message': message})

@app.route('/delete_url', methods=['POST'])
def remove_url():
	username = request.form.get('username')
	url = request.form.get('url')
	message = user_accounts.delete_url(username, url)
	return jsonify({'message': message})

@app.route('/admin/view_all_urls')
def admin_view_all_urls():
	urls = view_all_urls()
	return jsonify({'urls': urls})

@app.route('/admin/delete_url', methods=['POST'])
def admin_delete_url():
	url = request.form.get('url')
	message = delete_url(url)
	return jsonify({'message': message})

@app.route('/admin/delete_user', methods=['POST'])
def admin_delete_user():
	username = request.form.get('username')
	message = delete_user(username)
	return jsonify({'message': message})

@app.route('/admin/monitor_system')
def admin_monitor_system():
	data = monitor_system()
	return jsonify(data)

if __name__ == '__main__':
	app.run(debug=True)
