from flask import Flask, request, jsonify
from dataclasses import dataclass
import json
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Connect to SQLite database
try:
	conn = sqlite3.connect('database.db')
	c = conn.cursor()
except sqlite3.Error as e:
	print(e)

# Create tables
try:
	c.execute('''CREATE TABLE users
				(id text, username text, password text)''')
	c.execute('''CREATE TABLE transactions
				(id text, user_id text, amount real, category text, recurring boolean)''')
except sqlite3.OperationalError as e:
	print(e)

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
	try:
		data = request.get_json()
		data['password'] = generate_password_hash(data['password'])
		user = User(**data)
		c.execute("INSERT INTO users VALUES (:id, :username, :password)", {'id': user.id, 'username': user.username, 'password': user.password})
		conn.commit()
		return jsonify(user), 201
	except Exception as e:
		return str(e), 400

@app.route('/create_transaction', methods=['POST'])
def create_transaction():
	try:
		data = request.get_json()
		c.execute("SELECT password FROM users WHERE id = :user_id", {'user_id': data['user_id']})
		password_hash = c.fetchone()[0]
		if not check_password_hash(password_hash, data['password']):
			return 'Invalid password', 401
		transaction = Transaction(**data)
		c.execute("INSERT INTO transactions VALUES (:id, :user_id, :amount, :category, :recurring)", {'id': transaction.id, 'user_id': transaction.user_id, 'amount': transaction.amount, 'category': transaction.category, 'recurring': transaction.recurring})
		conn.commit()
		return jsonify(transaction), 201
	except Exception as e:
		return str(e), 400

if __name__ == '__main__':
	app.run(debug=True)
