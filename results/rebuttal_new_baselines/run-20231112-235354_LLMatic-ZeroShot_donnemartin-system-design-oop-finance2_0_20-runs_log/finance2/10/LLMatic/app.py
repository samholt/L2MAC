from flask import Flask, request
from models.user import User

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['username'], data['email'], data['password'])
	user.generate_verification_code()
	user.send_verification_code()
	return 'User registered successfully. Please check your email for the verification code.', 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = User(data['username'], data['email'], data['password'])
	if user.check_password(data['password']):
		user.generate_verification_code()
		user.send_verification_code()
		return 'Login successful. Please check your email for the verification code.', 200
	else:
		return 'Invalid credentials', 401

@app.route('/verify', methods=['POST'])
def verify():
	data = request.get_json()
	user = User(data['username'], data['email'], data['password'])
	if user.verify(data['verification_code']):
		return 'Verification successful', 200
	else:
		return 'Invalid verification code', 401

@app.route('/link_bank_account', methods=['POST'])
def link_bank_account():
	data = request.get_json()
	user = User(data['username'], data['email'], data['password'])
	user.link_bank_account(data['bank_account'])
	return 'Bank account linked successfully', 200

if __name__ == '__main__':
	app.run(debug=True)
