from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import requests
import sqlite3
from threading import Lock

app = Flask(__name__)

# Database connection
conn = sqlite3.connect('urls.db', check_same_thread=False)
c = conn.cursor()

# Create table
try:
	c.execute('''CREATE TABLE urls
			(original text, shortened text, clicks integer, created_at text, expires_at text, user_id text)''')
	conn.commit()
except sqlite3.OperationalError:
	pass

# Lock for thread-safe DB operations
lock = Lock()

@dataclass
class URL:
	original: str
	shortened: str
	clicks: int
	created_at: datetime
	expires_at: datetime
	user_id: str

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	short_url = data.get('short_url')
	user_id = data.get('user_id')
	expires_at = data.get('expires_at')

	# Validate URL
	try:
		response = requests.get(original_url)
		response.raise_for_status()
	except (requests.RequestException, ValueError):
		return jsonify({'error': 'Invalid URL'}), 400

	# Check if short URL is available
	with lock:
		c.execute('SELECT * FROM urls WHERE shortened=?', (short_url,))
		if c.fetchone() is not None:
			return jsonify({'error': 'Short URL already in use'}), 400

		# Create URL object and store in DB
		url = URL(original_url, short_url, 0, datetime.now(), expires_at, user_id)
		c.execute('INSERT INTO urls VALUES (?,?,?,?,?,?)', (url.original, url.shortened, url.clicks, url.created_at, url.expires_at, url.user_id))
		conn.commit()

	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	c.execute('SELECT * FROM urls WHERE shortened=?', (short_url,))
	url = c.fetchone()

	# Check if URL exists and has not expired
	if url is None or datetime.now() > datetime.fromisoformat(url[4]):
		return jsonify({'error': 'URL not found or expired'}), 404

	# Increment click count and redirect
	with lock:
		c.execute('UPDATE urls SET clicks = clicks + 1 WHERE shortened = ?', (short_url,))
		conn.commit()
	return redirect(url[0], code=302)

@app.route('/info/<short_url>', methods=['GET'])
def url_info(short_url):
	c.execute('SELECT * FROM urls WHERE shortened=?', (short_url,))
	url = c.fetchone()

	# Check if URL exists
	if url is None:
		return jsonify({'error': 'URL not found'}), 404

	# Return URL info
	return jsonify({'original': url[0], 'shortened': url[1], 'clicks': url[2], 'created_at': url[3], 'expires_at': url[4], 'user_id': url[5]}), 200

if __name__ == '__main__':
	app.run(debug=True)
