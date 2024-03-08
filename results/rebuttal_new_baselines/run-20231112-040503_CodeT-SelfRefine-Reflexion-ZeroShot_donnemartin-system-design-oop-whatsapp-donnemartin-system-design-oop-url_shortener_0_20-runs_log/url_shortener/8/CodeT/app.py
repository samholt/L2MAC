from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import uuid

app = Flask(__name__)

# Mock database
DB = {}

@dataclass
class URL:
	original: str
	shortened: str
	user: str
	clicks: []

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	user = data.get('user')
	shortened_url = str(uuid.uuid4())[:8]
	DB[shortened_url] = URL(original_url, shortened_url, user, [])
	return jsonify({'shortened_url': shortened_url}), 201

@app.route('/<shortened_url>', methods=['GET'])
def redirect_url(shortened_url):
	url = DB.get(shortened_url)
	if url:
		url.clicks.append(datetime.now())
		return redirect(url.original, code=302)
	else:
		return jsonify({'error': 'URL not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
