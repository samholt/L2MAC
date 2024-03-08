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
	clicks: int
	created_at: datetime
	expires_at: datetime

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	for url in DB.values():
		if url.original == data['original'] and url.user == data.get('user'):
			return jsonify({'shortened': url.shortened}), 200
	url = URL(
		original=data['original'],
		shortened=str(uuid.uuid4())[:8],
		user=data.get('user'),
		clicks=0,
		created_at=datetime.now(),
		expires_at=datetime.fromisoformat(data.get('expires_at'))
	)
	DB[url.shortened] = url
	return jsonify({'shortened': url.shortened}), 201

@app.route('/<shortened>', methods=['GET'])
def redirect_url(shortened):
	url = DB.get(shortened)
	if url and url.expires_at > datetime.now():
		url.clicks += 1
		return redirect(url.original, code=302)
	elif url:
		return jsonify({'error': 'URL expired'}), 404
	else:
		return jsonify({'error': 'URL not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
