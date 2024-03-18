from flask import Flask, redirect, request
import url_shortener
import analytics
import user_accounts
import admin_dashboard

app = Flask(__name__)

user_account = user_accounts.UserAccount()

@app.route('/<short_url>')
def redirect_to_url(short_url):
	ip_address = request.remote_addr
	analytics.track_click(short_url, ip_address)
	if short_url not in url_shortener.url_database or url_shortener.is_url_expired(short_url):
		return 'This URL is not found or has expired.', 404
	else:
		url_data = url_shortener.url_database[short_url]
		return redirect(url_data['url'], code=302)

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	url = request.json['url']
	custom_short_link = request.json.get('custom_short_link')
	expiration_date = request.json.get('expiration_date')
	short_url = url_shortener.generate_short_url(url, custom_short_link, expiration_date)
	return {'short_url': short_url}

@app.route('/analytics/<short_url>')
def get_analytics(short_url):
	return {'statistics': analytics.get_statistics(short_url)}

@app.route('/create_account', methods=['POST'])
def create_account():
	username = request.json['username']
	password = request.json['password']
	return {'message': user_account.create_account(username, password)}

@app.route('/admin/monitor_system')
def monitor_system():
	return admin_dashboard.monitor_system()

if __name__ == '__main__':
	app.run(debug=True)
