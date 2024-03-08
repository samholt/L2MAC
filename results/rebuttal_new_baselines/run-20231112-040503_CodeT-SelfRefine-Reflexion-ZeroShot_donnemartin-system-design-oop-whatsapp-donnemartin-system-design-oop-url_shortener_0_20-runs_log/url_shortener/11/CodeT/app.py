from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import uuid

app = Flask(__name__)

# Mock database
DB = {
	'users': {},
	'urls': {}
}

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
	clicks: list
	expiration_date: datetime

@app.route('/create_user', methods=['POST'])
def create_user():
	user_id = str(uuid.uuid4())
	DB['users'][user_id] = User(id=user_id, urls={})
	return jsonify({'user_id': user_id}), 201

@app.route('/create_url', methods=['POST'])
def create_url():
	data = request.get_json()
	user_id = data.get('user_id')
	original_url = data.get('original_url')
	short_url = data.get('short_url', str(uuid.uuid4())[:8])
	expiration_date = data.get('expiration_date')
	
	if expiration_date:
		expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d %H:%M:%S')
	
	url = URL(
		id=str(uuid.uuid4()),
		original_url=original_url,
		short_url=short_url,
		user_id=user_id,
		clicks=[],
		expiration_date=expiration_date
	)
	
	DB['users'][user_id].urls[short_url] = url
	DB['urls'][short_url] = url
	
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	url = DB['urls'].get(short_url)
	
	if not url:
		return jsonify({'error': 'URL not found'}), 404
	
	if url.expiration_date and url.expiration_date < datetime.now():
		return jsonify({'error': 'URL expired'}), 410
	
	url.clicks.append({'timestamp': datetime.now().isoformat()})
	
	return redirect(url.original_url, code=302)

@app.route('/analytics/<short_url>', methods=['GET'])
def get_analytics(short_url):
	url = DB['urls'].get(short_url)
	
	if not url:
		return jsonify({'error': 'URL not found'}), 404
	
	return jsonify({'clicks': url.clicks}), 200

if __name__ == '__main__':
	app.run(debug=True)
