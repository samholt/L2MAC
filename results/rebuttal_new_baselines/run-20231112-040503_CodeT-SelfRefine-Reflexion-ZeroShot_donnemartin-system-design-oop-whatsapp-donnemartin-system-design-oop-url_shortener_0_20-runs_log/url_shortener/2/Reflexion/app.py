from flask import Flask, request, redirect
from dataclasses import dataclass
from datetime import datetime
import json

app = Flask(__name__)

# Mock database
DATABASE = {}

@dataclass
class URL:
	original: str
	shortened: str
	expiration: datetime
	click_data: list

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	url = URL(data['original'], data['shortened'], datetime.strptime(data['expiration'], '%Y-%m-%d %H:%M:%S'), [])
	DATABASE[url.shortened] = url
	return {'shortened_url': url.shortened}, 200

@app.route('/<shortened>', methods=['GET'])
def redirect_to_original(shortened):
	url = DATABASE.get(shortened)
	if url and url.expiration > datetime.now():
		url.click_data.append({'click_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
		return redirect(url.original, code=302)
	else:
		return {'error': 'URL not found or expired'}, 404

@app.route('/analytics/<shortened>', methods=['GET'])
def get_analytics(shortened):
	url = DATABASE.get(shortened)
	if url:
		return {'click_data': url.click_data}, 200
	else:
		return {'error': 'URL not found'}, 404

if __name__ == '__main__':
	app.run(debug=True)
