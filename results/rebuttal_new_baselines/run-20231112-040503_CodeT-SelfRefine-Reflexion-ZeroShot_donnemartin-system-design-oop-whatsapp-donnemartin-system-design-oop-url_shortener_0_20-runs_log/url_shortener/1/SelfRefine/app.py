from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import uuid
import sqlite3

app = Flask(__name__)

# Database connection
conn = sqlite3.connect('urls.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS urls
              (original text, shortened text, user text, clicks integer, created_at timestamp, expires_at timestamp)''')
conn.commit()

@dataclass
class URL:
	original: str
	shortened: str
	user: str
	clicks: int
	created_at: datetime
	expires_at: datetime

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	user = data.get('user')
	expires_at = datetime.strptime(data.get('expires_at'), '%Y-%m-%d %H:%M:%S')
	shortened_url = str(uuid.uuid4())[:8]
	url = URL(original_url, shortened_url, user, 0, datetime.now(), expires_at)
	c.execute("INSERT INTO urls VALUES (?, ?, ?, ?, ?, ?)", (url.original, url.shortened, url.user, url.clicks, url.created_at, url.expires_at))
	conn.commit()
	return jsonify({'shortened_url': shortened_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	c.execute("SELECT * FROM urls WHERE shortened=?", (short_url,))
	url = c.fetchone()
	if url and url[5] > datetime.now():
		c.execute("UPDATE urls SET clicks = clicks + 1 WHERE shortened = ?", (short_url,))
		conn.commit()
		return redirect(url[0], code=302)
	else:
		return jsonify({'error': 'URL not found or expired'}), 404

if __name__ == '__main__':
	app.run(debug=True)
