from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
import datetime
import random
import string
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class URL(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	original = db.Column(db.String(500))
	short = db.Column(db.String(5))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	clicks = db.Column(db.Integer)
	created_at = db.Column(db.DateTime)
	expires_at = db.Column(db.DateTime)

	def __init__(self, original, short, user_id, clicks, created_at, expires_at):
		self.original = original
		self.short = short
		self.user_id = user_id
		self.clicks = clicks
		self.created_at = created_at
		self.expires_at = expires_at

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	password = db.Column(db.String(120))
	urls = db.relationship('URL', backref='user', lazy='dynamic')

	def __init__(self, username, password):
		self.username = username
		self.password = generate_password_hash(password)

@app.route('/shorten', methods=['POST'])
def shorten_url():
	try:
		data = request.get_json()
		original_url = data.get('url')
		user = User.query.filter_by(username=data.get('user')).first()
		expires_at = data.get('expires_at')
		short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		url = URL(original_url, short_url, user.id, 0, datetime.datetime.now(), expires_at)
		db.session.add(url)
		db.session.commit()
		return jsonify({'short_url': short_url}), 201
	except Exception as e:
		return jsonify({'error': str(e)}), 500

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	try:
		url = URL.query.filter_by(short=short_url).first()
		if url and url.expires_at > datetime.datetime.now():
			url.clicks += 1
			db.session.commit()
			return redirect(url.original, code=302)
		else:
			return jsonify({'error': 'URL not found or expired'}), 404
	except Exception as e:
		return jsonify({'error': str(e)}), 500

@app.route('/user', methods=['POST'])
def create_user():
	try:
		data = request.get_json()
		username = data.get('username')
		password = data.get('password')
		user = User(username, password)
		db.session.add(user)
		db.session.commit()
		return jsonify({'message': 'User created'}), 201
	except Exception as e:
		return jsonify({'error': str(e)}), 500

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
	try:
		user = User.query.filter_by(username=username).first()
		if user:
			return jsonify({'username': user.username, 'urls': [url.short for url in user.urls]}), 200
		else:
			return jsonify({'error': 'User not found'}), 404
	except Exception as e:
		return jsonify({'error': str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
	try:
		data = request.get_json()
		username = data.get('username')
		password = data.get('password')
		user = User.query.filter_by(username=username).first()
		if user and check_password_hash(user.password, password):
			return jsonify({'message': 'Login successful'}), 200
		else:
			return jsonify({'error': 'Invalid username or password'}), 401
	except Exception as e:
		return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
	app.run(debug=True)
