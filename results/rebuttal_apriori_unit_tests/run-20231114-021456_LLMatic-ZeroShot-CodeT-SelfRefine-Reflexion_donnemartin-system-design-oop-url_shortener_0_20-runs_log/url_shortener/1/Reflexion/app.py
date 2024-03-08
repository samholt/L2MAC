from flask import Flask, request, redirect, jsonify
import random
import string

app = Flask(__name__)

# Mock database
DATABASE = {}

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	url = request.json.get('url')
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	DATABASE[short_url] = url
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = DATABASE.get(short_url)
	if url:
		return redirect(url)
	else:
		return 'URL not found', 404
