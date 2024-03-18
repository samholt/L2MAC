from flask import Flask, request
from dataclasses import dataclass
import json
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# Mock database
users = {}
messages = {}

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(80), nullable=False)
	profile_picture = db.Column(db.String(120), nullable=True)
	status_message = db.Column(db.String(120), nullable=True)
	privacy_settings = db.Column(db.PickleType, nullable=True)

class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	from_user = db.Column(db.String(120), nullable=False)
	to_user = db.Column(db.String(120), nullable=False)
	message = db.Column(db.String(120), nullable=False)
	read = db.Column(db.Boolean, default=False)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if 'name' not in data or 'email' not in data or 'password' not in data:
		return {'status': 'failure', 'message': 'Missing required fields'}, 400
	data['password'] = generate_password_hash(data['password'])
	user = User(**data)
	db.session.add(user)
	db.session.commit()
	return {'status': 'success'}, 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')
	user = User.query.filter_by(email=email).first()
	if user and check_password_hash(user.password, password):
		return {'status': 'success'}, 200
	return {'status': 'failure'}, 401

@app.route('/message', methods=['POST'])
def message():
	data = request.get_json()
	if 'from_user' not in data or 'to_user' not in data or 'message' not in data:
		return {'status': 'failure', 'message': 'Missing required fields'}, 400
	message = Message(**data)
	db.session.add(message)
	db.session.commit()
	return {'status': 'success'}, 200

if __name__ == '__main__':
	app.run(debug=True)
