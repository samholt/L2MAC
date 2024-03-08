from flask import Flask, request, jsonify, session
from dataclasses import dataclass
import json
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

# Database connection
conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users
              (email text, password text)''')

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if 'email' not in data or 'password' not in data:
		return jsonify({'message': 'Missing email or password'}), 400
	c.execute('SELECT * FROM users WHERE email=?', (data['email'],))
	if c.fetchone() is not None:
		return jsonify({'message': 'Email already registered'}), 400
	hashed_password = generate_password_hash(data['password'])
	c.execute('INSERT INTO users VALUES (?,?)', (data['email'], hashed_password))
	conn.commit()
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if 'email' not in data or 'password' not in data:
		return jsonify({'message': 'Missing email or password'}), 400
	c.execute('SELECT * FROM users WHERE email=?', (data['email'],))
	user = c.fetchone()
	if user is None or not check_password_hash(user[1], data['password']):
		return jsonify({'message': 'Invalid email or password'}), 400
	session['logged_in'] = True
	session['email'] = data['email']
	return jsonify({'message': 'User logged in successfully'}), 200

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	session.pop('email', None)
	return jsonify({'message': 'User logged out successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
