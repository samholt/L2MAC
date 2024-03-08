from flask import Flask, render_template, request, redirect, url_for
import string
import random
import re
from datetime import datetime

app = Flask(__name__)

# Mock database
DATABASE = {
	'users': {},
	'urls': {},
	'clicks': {},
	'expirations': {}
}

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		DATABASE['users'][username] = password
		return redirect(url_for('login'))
	return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if DATABASE['users'].get(username) == password:
			return redirect(url_for('dashboard', username=username))
	return render_template('login.html')

@app.route('/dashboard/<username>')
def dashboard(username):
	return render_template('dashboard.html', username=username, urls=DATABASE['urls'].get(username, {}))

@app.route('/edit/<username>/<short_url>', methods=['GET', 'POST'])
def edit_url(username, short_url):
	if request.method == 'POST':
		new_url = request.form['url']
		DATABASE['urls'][username][short_url] = new_url
		return redirect(url_for('dashboard', username=username))
	return render_template('edit.html', username=username, short_url=short_url, url=DATABASE['urls'][username][short_url])

@app.route('/delete/<username>/<short_url>')
def delete_url(username, short_url):
	del DATABASE['urls'][username][short_url]
	return redirect(url_for('dashboard', username=username))

@app.route('/admin/delete_user/<username>')
def delete_user(username):
	del DATABASE['users'][username]
	return redirect(url_for('admin'))

@app.route('/admin/delete_url/<username>/<short_url>')
def delete_admin_url(username, short_url):
	del DATABASE['urls'][username][short_url]
	return redirect(url_for('admin'))

@app.route('/admin')
def admin():
	return render_template('admin.html', users=DATABASE['users'], urls=DATABASE['urls'])

@app.route('/<short_url>')
def redirect_to_url(short_url):
	for username, user_urls in DATABASE['urls'].items():
		if short_url in user_urls:
			# Check if URL has expired
			if DATABASE['expirations'].get(short_url) and DATABASE['expirations'][short_url] < datetime.now():
				# Delete expired URL
				del DATABASE['urls'][username][short_url]
				del DATABASE['expirations'][short_url]
				return 'URL has expired', 410
			# Record click information
			DATABASE['clicks'].setdefault(short_url, []).append({
				'date_time': datetime.now().isoformat(),
				'ip': request.remote_addr
			})
			return redirect(user_urls[short_url])
	return 'URL not found', 404

@app.route('/submit', methods=['POST'])
def submit_url():
	original_url = request.form['url']
	username = request.form['username']
	custom_short_url = request.form.get('custom_short_url')
	expiration_date = request.form.get('expiration_date')

	# Validate URL
	regex = re.compile(
		'^(?:http|ftp)s?://' # http:// or https://
		'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\\.)+(?:[A-Z]{2,6}\\.?|[A-Z0-9-]{2,}\\.?)|' # domain...
		'localhost|' # localhost...
		'\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})' # ...or ip
		'(?::\\d+)?' # optional port
		'(?:/?|[/?]\\S+)$', re.IGNORECASE)
	if re.match(regex, original_url) is None:
		return 'Invalid URL'

	# Generate short URL
	short_url = custom_short_url if custom_short_url else ''.join(random.choices(string.ascii_letters + string.digits, k=6))
	DATABASE['urls'].setdefault(username, {})[short_url] = original_url

	# Set expiration date if provided
	if expiration_date:
		DATABASE['expirations'][short_url] = datetime.strptime(expiration_date, '%Y-%m-%d %H:%M:%S')

	return redirect(url_for('dashboard', username=username))

@app.route('/analytics/<short_url>')
def analytics(short_url):
	clicks = DATABASE['clicks'].get(short_url, [])
	return render_template('analytics.html', short_url=short_url, clicks=clicks)

if __name__ == '__main__':
	app.run(debug=True)
