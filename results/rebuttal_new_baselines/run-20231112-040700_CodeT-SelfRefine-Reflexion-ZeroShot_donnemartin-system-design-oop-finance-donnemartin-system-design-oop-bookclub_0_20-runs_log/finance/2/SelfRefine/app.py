from flask import Flask, request, jsonify
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

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


class BankAccount(db.Model):
	id = db.Column(db.String, primary_key=True)
	user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)
	balance = db.Column(db.Float, nullable=False)


class Budget(db.Model):
	id = db.Column(db.String, primary_key=True)
	user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)
	category = db.Column(db.String(80), nullable=False)
	limit = db.Column(db.Float, nullable=False)


class Investment(db.Model):
	id = db.Column(db.String, primary_key=True)
	user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)
	value = db.Column(db.Float, nullable=False)


@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	if 'username' not in data or 'password' not in data or 'id' not in data:
		return jsonify({'message': 'Missing required fields'}), 400
	if User.query.filter_by(username=data['username']).first() is not None:
		return jsonify({'message': 'User already exists'}), 400
	user = User(**data)
	db.session.add(user)
	db.session.commit()
	return jsonify(user.id), 201

@app.route('/create_transaction', methods=['POST'])
def create_transaction():
	data = request.get_json()
	transaction = Transaction(**data)
	db.session.add(transaction)
	db.session.commit()
	return jsonify(transaction.id), 201

@app.route('/create_bank_account', methods=['POST'])
def create_bank_account():
	data = request.get_json()
	bank_account = BankAccount(**data)
	db.session.add(bank_account)
	db.session.commit()
	return jsonify(bank_account.id), 201

@app.route('/create_budget', methods=['POST'])
def create_budget():
	data = request.get_json()
	budget = Budget(**data)
	db.session.add(budget)
	db.session.commit()
	return jsonify(budget.id), 201

@app.route('/create_investment', methods=['POST'])
def create_investment():
	data = request.get_json()
	investment = Investment(**data)
	db.session.add(investment)
	db.session.commit()
	return jsonify(investment.id), 201

if __name__ == '__main__':
	app.run(debug=True)
