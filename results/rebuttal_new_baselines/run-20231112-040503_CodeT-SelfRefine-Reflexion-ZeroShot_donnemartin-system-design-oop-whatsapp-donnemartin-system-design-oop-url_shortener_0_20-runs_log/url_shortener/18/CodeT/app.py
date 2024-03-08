from flask import Flask, request, redirect, jsonify
from dataclasses import dataclass
from typing import Dict, List
import datetime
import random
import string

app = Flask(__name__)

# Mock database
users = {}
urls = {}

@dataclass
class User:
	id: str
	urls: Dict[str, str]

@dataclass
class URL:
	original_url: str
	short_url: str
	user_id: str
	clicks: List[datetime.datetime]

@app.route('/create_user', methods=['POST'])
def create_user():
	user_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
	users[user_id] = User(user_id, {})
	return jsonify({'user_id': user_id}), 201

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data['original_url']
	user_id = data['user_id']
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	urls[short_url] = URL(original_url, short_url, user_id, [])
	users[user_id].urls[short_url] = original_url
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	if short_url in urls:
		urls[short_url].clicks.append(datetime.datetime.now())
		return redirect(urls[short_url].original_url, code=302)
	else:
		return 'URL not found', 404

@app.route('/analytics', methods=['GET'])
def get_analytics():
	data = request.get_json()
	user_id = data['user_id']
	user_urls = users[user_id].urls
	analytics = {}
	for short_url, original_url in user_urls.items():
		analytics[short_url] = {'original_url': original_url, 'clicks': len(urls[short_url].clicks)}
	return jsonify(analytics), 200

if __name__ == '__main__':
	app.run(debug=True)
