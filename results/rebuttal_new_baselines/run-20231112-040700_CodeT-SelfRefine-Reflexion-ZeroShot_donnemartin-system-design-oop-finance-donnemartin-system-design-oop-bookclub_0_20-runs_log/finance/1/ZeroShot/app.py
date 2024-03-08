from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DATABASE = {}

@dataclass
class User:
	username: str
	password: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	DATABASE[user.username] = user
	return jsonify({'message': 'User registered successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
