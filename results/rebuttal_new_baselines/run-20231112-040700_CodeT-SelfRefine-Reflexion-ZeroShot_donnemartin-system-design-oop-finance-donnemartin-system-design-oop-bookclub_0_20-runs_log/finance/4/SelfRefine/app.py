from flask import Flask, request, jsonify
from dataclasses import dataclass
import json
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# Database models
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	password = db.Column(db.String(120), nullable=False)

def __repr__(self):
	return '<User %r>' % self.username

class Transaction(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.String(80), db.ForeignKey('user.username'), nullable=False)
	type = db.Column(db.String(80), nullable=False)
	amount = db.Column(db.Float, nullable=False)
	category = db.Column(db.String(80), nullable=False)

def __repr__(self):
	return '<Transaction %r>' % self.id

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	if User.query.filter_by(username=data.get('username')).first() is not None:
		return jsonify({'message': 'User already exists'}), 400
	data['password'] = generate_password_hash(data['password'], method='sha256')
	user = User(**data)
	db.session.add(user)
	db.session.commit()
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = User.query.filter_by(username=data.get('username')).first()
	if user and check_password_hash(user.password, data.get('password')):
		return jsonify({'message': 'Login successful'}), 200
	return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
	data = request.get_json()
	if User.query.filter_by(username=data.get('user_id')).first() is None:
		return jsonify({'message': 'User does not exist'}), 400
	transaction = Transaction(**data)
	db.session.add(transaction)
	db.session.commit()
	return jsonify({'message': 'Transaction added successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
