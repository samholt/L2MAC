from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)

users = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data.get('username')
	email = data.get('email')
	password = data.get('password')
	if username and email and password:
		if email not in users:
			users[email] = {'username': username, 'password': password}
			return jsonify({'message': 'User registered successfully'}), 200
		else:
			return jsonify({'message': 'User already exists'}), 400
	else:
		return jsonify({'message': 'Invalid data'}), 400

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')
	if email and password:
		user = users.get(email)
		if user and user['password'] == password:
			token = jwt.encode({'user': email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
			return jsonify({'token': token.decode('UTF-8')}), 200
		else:
			return jsonify({'message': 'Invalid credentials'}), 400
	else:
		return jsonify({'message': 'Invalid data'}), 400

if __name__ == '__main__':
	app.config['SECRET_KEY'] = 'thisissecret'
	app.run(port=5002)

