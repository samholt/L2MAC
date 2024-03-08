from flask import Flask, request, jsonify
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# Database models

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	password = db.Column(db.String(120), nullable=False)


class Transaction(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.String(80), db.ForeignKey('user.username'), nullable=False)
	type = db.Column(db.String(80), nullable=False)
	amount = db.Column(db.Float, nullable=False)
	category = db.Column(db.String(80), nullable=False)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	try:
		db.session.add(user)
		db.session.commit()
		return jsonify({'message': 'User registered successfully'}), 201
	except IntegrityError:
		return jsonify({'message': 'Username already exists'}), 400

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = User.query.filter_by(username=data.get('username')).first()
	if user and user.password == data.get('password'):
		return jsonify({'message': 'Logged in successfully'}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/transaction', methods=['POST'])
def add_transaction():
	data = request.get_json()
	user = User.query.filter_by(username=data.get('user_id')).first()
	if not user:
		return jsonify({'message': 'User does not exist'}), 400
	transaction = Transaction(**data)
	db.session.add(transaction)
	db.session.commit()
	return jsonify({'message': 'Transaction added successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
