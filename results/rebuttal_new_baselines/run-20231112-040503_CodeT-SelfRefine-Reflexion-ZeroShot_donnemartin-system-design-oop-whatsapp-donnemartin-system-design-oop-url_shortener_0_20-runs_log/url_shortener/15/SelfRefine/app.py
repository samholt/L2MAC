from flask import Flask, request, redirect, jsonify
from dataclasses import dataclass
from datetime import datetime
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

# Mock database
users = {}
urls = {}

@dataclass
class User:
	id: str
	username: str
	password: str
	urls: dict

@dataclass
class URL:
	id: str
	original_url: str
	short_url: str
	user_id: str
	clicks: list
	expiration_date: datetime

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	for user in users.values():
		if user.username == data['username']:
			return jsonify({'message': 'Username already exists'}), 400
	user_id = str(uuid.uuid4())
	password_hash = generate_password_hash(data['password'])
	user = User(id=user_id, username=data['username'], password=password_hash, urls={})
	users[user_id] = user
	return jsonify({'message': 'User registered successfully', 'user_id': user_id}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	for user in users.values():
		if user.username == data['username'] and check_password_hash(user.password, data['password']):
			access_token = create_access_token(identity=user.id)
			return jsonify({'message': 'Logged in successfully', 'access_token': access_token}), 200
	return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/shorten_url', methods=['POST'])
@jwt_required
def shorten_url():
	data = request.get_json()
	url_id = str(uuid.uuid4())
	short_url = f'http://short.en/{url_id}'
	url = URL(id=url_id, original_url=data['original_url'], short_url=short_url, user_id=data['user_id'], clicks=[], expiration_date=data.get('expiration_date'))
	urls[url_id] = url
	users[data['user_id']].urls[url_id] = url
	return jsonify({'message': 'URL shortened successfully', 'short_url': short_url}), 201

@app.route('/<url_id>', methods=['GET'])
def redirect_url(url_id):
	url = urls.get(url_id)
	if url and (not url.expiration_date or url.expiration_date > datetime.now()):
		url.clicks.append({'click_time': datetime.now().isoformat()})
		return redirect(url.original_url, code=302)
	return jsonify({'message': 'URL not found or expired'}), 404

@app.route('/analytics/<url_id>', methods=['GET'])
@jwt_required
def get_analytics(url_id):
	url = urls.get(url_id)
	if url:
		return jsonify({'message': 'URL analytics', 'clicks': url.clicks}), 200
	return jsonify({'message': 'URL not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
