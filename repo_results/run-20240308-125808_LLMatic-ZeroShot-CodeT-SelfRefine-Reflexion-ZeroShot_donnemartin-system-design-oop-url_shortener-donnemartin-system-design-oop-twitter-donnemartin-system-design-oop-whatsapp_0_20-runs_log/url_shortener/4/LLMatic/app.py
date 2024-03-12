from flask import Flask, redirect, abort, request
import url_shortener as us
import analytics as an
import user_accounts as ua_module
import admin_dashboard as ad

app = Flask(__name__)
ua = ua_module.UserAccounts()

@app.route('/')
def home():
	return 'Hello, World!', 200

@app.route('/<short_url>')
def redirect_to_url(short_url):
	url = us.get_original_url(short_url)
	if url == '404: URL not found or expired':
		abort(404)
	else:
		return redirect(url, code=302)

@app.route('/shorten', methods=['POST'])
def shorten_url():
	url = request.json['url']
	short_url = us.generate_short_url(url)
	return {'short_url': short_url}, 200

@app.route('/analytics/<short_url>')
def get_analytics(short_url):
	click_count = an.get_click_count(short_url)
	click_details = an.get_click_details(short_url)
	return {'click_count': click_count, 'click_details': click_details}, 200

@app.route('/user', methods=['POST'])
def create_user():
	username = request.json['username']
	message = ua.create_account(username)
	return {'message': message}, 200

@app.route('/admin/urls')
def get_all_urls():
	urls = ad.get_all_urls()
	return {'urls': urls}, 200

if __name__ == '__main__':
	app.run(debug=True)
