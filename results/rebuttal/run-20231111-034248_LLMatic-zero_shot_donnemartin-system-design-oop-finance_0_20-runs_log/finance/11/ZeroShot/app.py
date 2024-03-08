from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DB = {}

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

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	DB[user.id] = user
	return jsonify(user), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = DB.get(data['id'])
	if user and user.password == data['password']:
		return jsonify(user), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/transaction', methods=['POST'])
def add_transaction():
	data = request.get_json()
	transaction = Transaction(**data)
	DB[transaction.id] = transaction
	return jsonify(transaction), 201

if __name__ == '__main__':
	app.run(debug=True)
