from flask import Flask, request, jsonify
from dataclasses import dataclass
import json
import sqlite3
import hashlib

app = Flask(__name__)

# Database connection
try:
	conn = sqlite3.connect('database.db')
	c = conn.cursor()
except Exception as e:
	return jsonify({'message': 'Database connection failed', 'error': str(e)}), 500

# Create tables
try:
	c.execute('''CREATE TABLE users
				(username text, password text)''')
	c.execute('''CREATE TABLE transactions
				(user_id text, type text, amount real, category text)''')
except Exception as e:
	return jsonify({'message': 'Table creation failed', 'error': str(e)}), 500

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
	hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
	try:
		c.execute("INSERT INTO users VALUES (?,?)", (user.username, hashed_password))
		conn.commit()
	except Exception as e:
		return jsonify({'message': 'User creation failed', 'error': str(e)}), 500
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	hashed_password = hashlib.sha256(password.encode()).hexdigest()
	try:
		c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, hashed_password))
		user = c.fetchone()
	except Exception as e:
		return jsonify({'message': 'Login failed', 'error': str(e)}), 500
	if user:
		return jsonify({'message': 'Login successful'}), 200
	return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
	data = request.get_json()
	transaction = Transaction(**data)
	try:
		c.execute("INSERT INTO transactions VALUES (?,?,?,?)", (transaction.user_id, transaction.type, transaction.amount, transaction.category))
		conn.commit()
	except Exception as e:
		return jsonify({'message': 'Transaction addition failed', 'error': str(e)}), 500
	return jsonify({'message': 'Transaction added successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
