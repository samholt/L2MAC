from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import uuid
import sqlite3

app = Flask(__name__)

# Database connection
conn = sqlite3.connect('urls.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS urls
              (original text, shortened text, user text, clicks integer, click_data text, expiration text)''')
conn.commit()

@dataclass
class URL:
	original: str
	shortened: str
	user: str
	clicks: int
	click_data: list
	expiration: datetime

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	user = data.get('user')
	expiration = data.get('expiration')
	shortened_url = data.get('shortened', str(uuid.uuid4())[:8])
	c.execute("SELECT * FROM urls WHERE shortened=?", (shortened_url,))
	if c.fetchone() is not None:
		return jsonify({'error': 'Shortened URL already in use'}), 400
	c.execute("INSERT INTO urls VALUES (?, ?, ?, ?, ?, ?)", (original_url, shortened_url, user, 0, '[]', expiration))
	conn.commit()
	return jsonify({'shortened_url': shortened_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	c.execute("SELECT * FROM urls WHERE shortened=?", (short_url,))
	url = c.fetchone()
	if url and datetime.now() <= datetime.fromisoformat(url[5]):
		c.execute("UPDATE urls SET clicks = clicks + 1 WHERE shortened = ?", (short_url,))
		conn.commit()
		return redirect(url[0], code=302)
	else:
		return jsonify({'error': 'URL not found or expired'}), 404

@app.route('/analytics/<short_url>', methods=['GET'])
def get_analytics(short_url):
	c.execute("SELECT * FROM urls WHERE shortened=?", (short_url,))
	url = c.fetchone()
	if url:
		return jsonify({'clicks': url[3], 'click_data': url[4]}), 200
	else:
		return jsonify({'error': 'URL not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
