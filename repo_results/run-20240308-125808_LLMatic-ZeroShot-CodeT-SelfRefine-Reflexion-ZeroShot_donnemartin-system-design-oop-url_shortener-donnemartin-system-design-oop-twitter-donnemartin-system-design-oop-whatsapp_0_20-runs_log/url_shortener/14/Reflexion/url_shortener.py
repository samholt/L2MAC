from flask import Flask, request, redirect, jsonify
import re
import random
import string
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DATABASE = {}

@dataclass
class URL:
	original: str
	shortened: str
	clicks: int


@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	custom_alias = data.get('alias')

	if not is_valid_url(original_url):
		return jsonify({'error': 'Invalid URL'}), 400

	shortened_url = custom_alias if custom_alias else generate_short_url()
	while shortened_url in DATABASE:
		shortened_url = generate_short_url()

	DATABASE[shortened_url] = URL(original_url, shortened_url, 0)

	return jsonify({'shortened_url': shortened_url}), 200


@app.route('/<short_url>', methods=['GET'])
def redirect_to_original(short_url):
	url = DATABASE.get(short_url)

	if not url:
		return jsonify({'error': 'URL not found'}), 404

	url.clicks += 1
	return redirect(url.original, code=302)


@app.route('/stats/<short_url>', methods=['GET'])
def get_url_stats(short_url):
	url = DATABASE.get(short_url)

	if not url:
		return jsonify({'error': 'URL not found'}), 404

	return jsonify({'original_url': url.original, 'clicks': url.clicks}), 200


def is_valid_url(url):
	regex = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
	return re.match(regex, url) is not None


def generate_short_url():
	return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


if __name__ == '__main__':
	app.run(debug=True)
