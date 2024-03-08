from flask import Flask, request, jsonify
from dataclasses import dataclass
import json
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Database connection
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create tables if they do not exist
try:
	c.execute('''CREATE TABLE IF NOT EXISTS users
			 (id text, username text, password text)''')
	c.execute('''CREATE TABLE IF NOT EXISTS transactions
			 (id text, user_id text, amount real, category text, recurring bool)''')
except sqlite3.Error as e:
	print(f'Error {e}')

@dataclass
class User:
	id: str
	username: str
	password: str

@dataclass
class Transaction:
	id: str
	user_id: str
	amount: float
	category: str
	recurring: bool

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	user.password = generate_password_hash(user.password)
	try:
		c.execute("INSERT INTO users VALUES (?, ?, ?)", (user.id, user.username, user.password))
		conn.commit()
	except sqlite3.Error as e:
		return jsonify({'error': str(e)}), 500
	return jsonify(user), 201

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
	data = request.get_json()
	transaction = Transaction(**data)
	try:
		c.execute("INSERT INTO transactions VALUES (?, ?, ?, ?, ?)", (transaction.id, transaction.user_id, transaction.amount, transaction.category, transaction.recurring))
		conn.commit()
	except sqlite3.Error as e:
		return jsonify({'error': str(e)}), 500
	return jsonify(transaction), 201

if __name__ == '__main__':
	app.run(debug=True)
