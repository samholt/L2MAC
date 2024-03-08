from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict
import sqlite3

app = Flask(__name__)

# Database connection
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create tables
try:
	c.execute('''CREATE TABLE users
				(username text, password text)''')
	c.execute('''CREATE TABLE transactions
				(user_id text, type text, amount real, category text)''')
except:
	pass

@dataclass
class User:
	username: str
	password: str

@dataclass
class Transaction:
	user_id: str
	type: str
	amount: float
	category: str

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	c.execute("SELECT * FROM users WHERE username=?", (user.username,))
	if c.fetchone() is not None:
		return jsonify({'message': 'User already exists'}), 400
	c.execute("INSERT INTO users VALUES (?,?)", (user.username, user.password))
	conn.commit()
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
	data = request.get_json()
	transaction = Transaction(**data)
	c.execute("SELECT * FROM users WHERE username=?", (transaction.user_id,))
	if c.fetchone() is None:
		return jsonify({'message': 'User does not exist'}), 400
	c.execute("INSERT INTO transactions VALUES (?,?,?,?)", (transaction.user_id, transaction.type, transaction.amount, transaction.category))
	conn.commit()
	return jsonify({'message': 'Transaction added successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
