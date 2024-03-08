from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from typing import Dict, List
import datetime
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
	urls: Dict[str, str]

@dataclass
class URL:
	id: str
	original_url: str
	short_url: str
	user_id: str
	clicks: List[datetime.datetime]

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	user_id = data.get('user_id')
	original_url = data.get('original_url')
	short_url = data.get('short_url', str(uuid.uuid4())[:8])
	
	# Check if the short_url is already in use
	for url in DB['urls'].values():
		if url.short_url == short_url:
			return jsonify({'error': 'Short URL already in use'}), 400
	
	url = URL(id=str(uuid.uuid4()), original_url=original_url, short_url=short_url, user_id=user_id, clicks=[])
	DB['urls'][url.id] = url
	if user_id:
		DB['users'][user_id].urls[url.id] = url.short_url
	
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	for url in DB['urls'].values():
		if url.short_url == short_url:
			url.clicks.append(datetime.datetime.now())
			return redirect(url.original_url)
	
	return jsonify({'error': 'URL not found'}), 404

@app.route('/analytics', methods=['GET'])
def get_analytics():
	data = request.get_json()
	user_id = data.get('user_id')
	
	if user_id not in DB['users']:
		return jsonify({'error': 'User not found'}), 404
	
	analytics = {}
	for url_id, short_url in DB['users'][user_id].urls.items():
		url = DB['urls'][url_id]
		analytics[short_url] = len(url.clicks)
	
	return jsonify(analytics), 200

@app.route('/users', methods=['POST'])
def create_user():
	user = User(id=str(uuid.uuid4()), urls={})
	DB['users'][user.id] = user
	return jsonify({'user_id': user.id}), 201

if __name__ == '__main__':
	app.run(debug=True)
