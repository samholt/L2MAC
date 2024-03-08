from flask import Flask, request, jsonify
from dataclasses import dataclass
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

users = {}
sessions = {}

@dataclass
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(80), nullable=False)
	profile_picture = db.Column(db.String(120), nullable=True)
	status_message = db.Column(db.String(120), nullable=True)
	privacy_settings = db.Column(db.String(120), nullable=True)

@app.route('/signup', methods=['POST'])
def signup():
	data = request.get_json()
	existing_user = User.query.filter_by(email=data['email']).first()
	if existing_user is not None:
		return jsonify({'message': 'Email already in use'}), 400
	user = User(**data)
	try:
		db.session.add(user)
		db.session.commit()
		return jsonify({'message': 'User created successfully'}), 201
	except Exception as e:
		return jsonify({'message': 'Error creating user', 'error': str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = User.query.filter_by(email=data['email']).first()
	if user and user.password == data['password']:
		sessions[data['email']] = 'Logged In'
		return jsonify({'message': 'Logged in successfully'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/logout', methods=['POST'])
def logout():
	data = request.get_json()
	sessions.pop(data['email'], None)
	return jsonify({'message': 'Logged out successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
