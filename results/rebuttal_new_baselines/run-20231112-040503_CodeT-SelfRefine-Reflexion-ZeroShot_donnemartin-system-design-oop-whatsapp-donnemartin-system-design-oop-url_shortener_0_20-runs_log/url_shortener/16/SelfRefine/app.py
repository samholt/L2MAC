from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import uuid
import sqlite3
from contextlib import closing

app = Flask(__name__)

# Database connection
DATABASE = 'database.db'

# Create tables
with closing(sqlite3.connect(DATABASE)) as db:
	with closing(db.cursor()) as cursor:
		try:
			cursor.execute('''CREATE TABLE users
				 (id text primary key, urls text)''')
			cursor.execute('''CREATE TABLE urls
				 (id text primary key, original_url text, short_url text, user_id text, clicks integer, click_data text, expiration_date text)''')
			db.commit()
		except sqlite3.OperationalError:
			pass

@dataclass
class User:
	id: str
	urls: dict

@dataclass
class URL:
	id: str
	original_url: str
	short_url: str
	user_id: str
	clicks: int
	click_data: list
	expiration_date: datetime

@app.route('/create_user', methods=['POST'])
def create_user():
	user_id = str(uuid.uuid4())
	with closing(sqlite3.connect(DATABASE)) as db:
		with closing(db.cursor()) as cursor:
			cursor.execute("INSERT INTO users VALUES (?, ?)", (user_id, '{}'))
			db.commit()
	return jsonify({'user_id': user_id}), 201

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	user_id = data.get('user_id')
	original_url = data.get('original_url')
	short_url = data.get('short_url', str(uuid.uuid4())[:8])
	expiration_date = data.get('expiration_date')
	if expiration_date:
		expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d %H:%M:%S')
	url_id = str(uuid.uuid4())
	with closing(sqlite3.connect(DATABASE)) as db:
		with closing(db.cursor()) as cursor:
			cursor.execute("INSERT INTO urls VALUES (?, ?, ?, ?, ?, ?, ?)", (url_id, original_url, short_url, user_id, 0, '[]', expiration_date))
			db.commit()
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	with closing(sqlite3.connect(DATABASE)) as db:
		with closing(db.cursor()) as cursor:
			cursor.execute("SELECT * FROM urls WHERE short_url = ?", (short_url,))
			url = cursor.fetchone()
		if url:
			if url[6] and datetime.strptime(url[6], '%Y-%m-%d %H:%M:%S') < datetime.now():
				return jsonify({'error': 'URL expired'}), 400
			clicks = url[4] + 1
			click_data = eval(url[5])
			click_data.append({'click_time': datetime.now().isoformat()})
			with closing(sqlite3.connect(DATABASE)) as db:
				with closing(db.cursor()) as cursor:
					cursor.execute("UPDATE urls SET clicks = ?, click_data = ? WHERE id = ?", (clicks, str(click_data), url[0]))
					db.commit()
			return redirect(url[1])
	return jsonify({'error': 'URL not found'}), 404

@app.route('/analytics', methods=['GET'])
def get_analytics():
	data = request.get_json()
	user_id = data.get('user_id')
	with closing(sqlite3.connect(DATABASE)) as db:
		with closing(db.cursor()) as cursor:
			cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
			user = cursor.fetchone()
		if not user:
			return jsonify({'error': 'User not found'}), 404
		cursor.execute("SELECT * FROM urls WHERE user_id = ?", (user_id,))
		urls = cursor.fetchall()
	analytics = {}
	for url in urls:
		analytics[url[2]] = {'clicks': url[4], 'click_data': eval(url[5])}
	return jsonify(analytics), 200

if __name__ == '__main__':
	app.run(debug=True)
