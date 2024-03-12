from flask import Flask, request, redirect, jsonify
from dataclasses import dataclass
from datetime import datetime
import requests
import sqlite3
from threading import Lock

app = Flask(__name__)

# Database connection
conn = sqlite3.connect('database.db', check_same_thread=False)
c = conn.cursor()

# Create tables
try:
	c.execute('''CREATE TABLE users
			 (username text, password text)''')
	c.execute('''CREATE TABLE urls
			 (original_url text, short_url text, user text, clicks text, expiration_date text)''')
except:
	pass

# Lock for handling concurrent requests
lock = Lock()

@dataclass
class User:
	username: str
	password: str

@dataclass
class URL:
	original_url: str
	short_url: str
	user: str
	clicks: list
	expiration_date: datetime

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	password = data['password']
	c.execute('SELECT * FROM users WHERE username=?', (username,))
	if c.fetchone() is not None:
		return jsonify({'message': 'Username already exists'}), 400
	c.execute('INSERT INTO users VALUES (?,?)', (username, password))
	conn.commit()
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
	if c.fetchone() is None:
		return jsonify({'message': 'Invalid username or password'}), 400
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/shorten', methods=['POST'])
def shorten():
	data = request.get_json()
	original_url = data['original_url']
	short_url = data['short_url']
	username = data['username']
	expiration_date = datetime.strptime(data['expiration_date'], '%Y-%m-%d %H:%M:%S')
	lock.acquire()
	c.execute('SELECT * FROM urls WHERE short_url=?', (short_url,))
	if c.fetchone() is not None:
		lock.release()
		return jsonify({'message': 'Short URL already exists'}), 400
	try:
		response = requests.get(original_url)
		if response.status_code != 200:
			lock.release()
			return jsonify({'message': 'Invalid original URL'}), 400
	except:
		lock.release()
		return jsonify({'message': 'Invalid original URL'}), 400
	c.execute('INSERT INTO urls VALUES (?,?,?,?,?)', (original_url, short_url, username, '[]', str(expiration_date)))
	conn.commit()
	lock.release()
	return jsonify({'message': 'URL shortened successfully'}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_to_original(short_url):
	c.execute('SELECT * FROM urls WHERE short_url=?', (short_url,))
	url = c.fetchone()
	if url is None or datetime.now() > datetime.strptime(url[4], '%Y-%m-%d %H:%M:%S'):
		return jsonify({'message': 'Invalid or expired short URL'}), 400
	clicks = eval(url[3])
	clicks.append((str(datetime.now()), request.remote_addr))
	c.execute('UPDATE urls SET clicks=? WHERE short_url=?', (str(clicks), short_url))
	conn.commit()
	return redirect(url[0], code=302)

@app.route('/analytics', methods=['GET'])
def analytics():
	data = request.get_json()
	username = data['username']
	c.execute('SELECT * FROM users WHERE username=?', (username,))
	if c.fetchone() is None:
		return jsonify({'message': 'Invalid username'}), 400
	c.execute('SELECT * FROM urls WHERE user=?', (username,))
	user_urls = c.fetchall()
	analytics_data = {}
	for url in user_urls:
		analytics_data[url[1]] = {'clicks': len(eval(url[3])), 'details': eval(url[3])}
	return jsonify(analytics_data), 200

if __name__ == '__main__':
	app.run(debug=True)
