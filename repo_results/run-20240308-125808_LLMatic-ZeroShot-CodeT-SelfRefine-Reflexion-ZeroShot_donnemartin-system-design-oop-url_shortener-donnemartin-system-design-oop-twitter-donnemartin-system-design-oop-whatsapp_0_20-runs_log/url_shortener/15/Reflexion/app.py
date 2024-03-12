from flask import Flask, request, redirect
from database import Database
from models import User, URL
import uuid
import datetime


app = Flask(__name__)
db = Database()


@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('original_url')
	custom_link = data.get('custom_link')
	expiration = data.get('expiration')
	user_id = data.get('user_id')
	shortened_url = custom_link if custom_link else str(uuid.uuid4())[:8]
	url = URL(id=shortened_url, original_url=original_url, shortened_url=shortened_url, user_id=user_id, clicks=[], expiration=expiration)
	db.add_url(url)
	return {'shortened_url': shortened_url}, 200


@app.route('/<shortened_url>', methods=['GET'])
def redirect_to_original(shortened_url):
	url = db.get_url(shortened_url)
	if url and (not url.expiration or datetime.datetime.now() < datetime.datetime.strptime(url.expiration, '%Y-%m-%d %H:%M:%S')):
		url.clicks.append({'timestamp': str(datetime.datetime.now()), 'location': request.remote_addr})
		return redirect(url.original_url, code=302)
	else:
		return {'error': 'URL not found or expired'}, 404


@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	user = User(id=str(uuid.uuid4()), username=username, password=password, urls=[])
	db.add_user(user)
	return {'user_id': user.id}, 200


@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	for user in db.users.values():
		if user.username == username and user.password == password:
			return {'user_id': user.id}, 200
	return {'error': 'Invalid credentials'}, 401


@app.route('/admin', methods=['GET'])
def admin():
	return {'users': db.users, 'urls': db.urls}, 200


if __name__ == '__main__':
	app.run(debug=True)

