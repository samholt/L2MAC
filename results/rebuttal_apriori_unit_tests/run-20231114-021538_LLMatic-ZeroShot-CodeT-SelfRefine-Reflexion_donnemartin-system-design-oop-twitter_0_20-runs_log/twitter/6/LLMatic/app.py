from flask import Flask, request
from models import User

app = Flask(__name__)

users = {}

@app.route('/register', methods=['POST'])
def register():
	username = request.form['username']
	email = request.form['email']
	password = request.form['password']
	user = User(len(users) + 1, username, email, password)
	users[email] = user
	return 'User registered successfully', 200

if __name__ == '__main__':
	app.run(debug=True)
