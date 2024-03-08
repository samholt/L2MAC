from flask import Flask, request
from user import User

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['email'], data['username'], data['password'])
	return user.register()

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = User(None, data['username'], data['password'])
	return user.authenticate(data['username'], data['password'])

@app.route('/reset_password', methods=['POST'])
def reset_password():
	data = request.get_json()
	user = User(None, data['username'], None)
	return user.reset_password(data['username'], data['new_password'])

if __name__ == '__main__':
	app.run(debug=True)
