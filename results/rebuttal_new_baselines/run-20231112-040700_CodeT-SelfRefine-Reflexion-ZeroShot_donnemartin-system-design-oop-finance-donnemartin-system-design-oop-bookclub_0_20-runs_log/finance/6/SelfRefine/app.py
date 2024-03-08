from flask import Flask, request, jsonify
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
	id = db.Column(db.String, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	password = db.Column(db.String(120), nullable=False)


class Transaction(db.Model):
	id = db.Column(db.String, primary_key=True)
	user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)
	amount = db.Column(db.Float, nullable=False)
	category = db.Column(db.String(80), nullable=False)
	recurring = db.Column(db.Boolean, nullable=False)

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	if 'id' not in data or 'username' not in data or 'password' not in data:
		return jsonify({'error': 'Missing required field'}), 400
	user = User(**data)
	try:
		db.session.add(user)
		db.session.commit()
		return jsonify(user.id), 201
	except IntegrityError:
		return jsonify({'error': 'Username already exists'}), 400

@app.route('/create_transaction', methods=['POST'])
def create_transaction():
	data = request.get_json()
	if 'id' not in data or 'user_id' not in data or 'amount' not in data or 'category' not in data or 'recurring' not in data:
		return jsonify({'error': 'Missing required field'}), 400
	transaction = Transaction(**data)
	try:
		db.session.add(transaction)
		db.session.commit()
		return jsonify(transaction.id), 201
	except IntegrityError:
		return jsonify({'error': 'Transaction already exists'}), 400

if __name__ == '__main__':
	app.run(debug=True)
