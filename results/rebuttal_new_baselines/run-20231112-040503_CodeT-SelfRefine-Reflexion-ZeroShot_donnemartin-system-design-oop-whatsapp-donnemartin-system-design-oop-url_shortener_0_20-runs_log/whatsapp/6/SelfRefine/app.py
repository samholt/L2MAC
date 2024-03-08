from flask import Flask, request
from dataclasses import dataclass
import json
import sqlite3
import hashlib
from flask_limiter import Limiter

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)

conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE users
              (email text, password text)''')
conn.commit()

@app.route('/register', methods=['POST'])
@limiter.limit('5/minute')
def register():
	data = request.get_json()
	if 'email' not in data or 'password' not in data:
		return {'error': 'Email and password required'}, 400
	c.execute("SELECT * FROM users WHERE email=?", (data['email'],))
	if c.fetchone() is not None:
		return {'error': 'Email already registered'}, 400
	hashed_password = hashlib.sha256(data['password'].encode()).hexdigest()
	c.execute("INSERT INTO users VALUES (?,?)", (data['email'], hashed_password))
	conn.commit()
	return {'message': 'User registered successfully'}, 200

@app.route('/login', methods=['POST'])
@limiter.limit('5/minute')
def login():
	data = request.get_json()
	if 'email' not in data or 'password' not in data:
		return {'error': 'Email and password required'}, 400
	hashed_password = hashlib.sha256(data['password'].encode()).hexdigest()
	c.execute("SELECT * FROM users WHERE email=? AND password=?", (data['email'], hashed_password))
	if c.fetchone() is None:
		return {'error': 'Invalid email or password'}, 400
	return {'message': 'User logged in successfully'}, 200

if __name__ == '__main__':
	app.run(debug=True)
