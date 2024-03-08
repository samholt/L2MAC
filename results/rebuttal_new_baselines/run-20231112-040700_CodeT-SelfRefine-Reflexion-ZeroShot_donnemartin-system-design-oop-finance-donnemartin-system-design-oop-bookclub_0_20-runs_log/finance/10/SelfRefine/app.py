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
	user_id = db.Column(db.String, db.ForeignKey('user.id'))
	amount = db.Column(db.Float, nullable=False)
	category = db.Column(db.String(80), nullable=False)

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	try:
		db.session.add(user)
		db.session.commit()
	except IntegrityError:
		return jsonify('A user with this ID already exists'), 400
	return jsonify(user.id), 201

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
	data = request.get_json()
	transaction = Transaction(**data)
	try:
		db.session.add(transaction)
		db.session.commit()
	except IntegrityError:
		return jsonify('A transaction with this ID already exists'), 400
	return jsonify(transaction.id), 201

if __name__ == '__main__':
	app.run(debug=True)
