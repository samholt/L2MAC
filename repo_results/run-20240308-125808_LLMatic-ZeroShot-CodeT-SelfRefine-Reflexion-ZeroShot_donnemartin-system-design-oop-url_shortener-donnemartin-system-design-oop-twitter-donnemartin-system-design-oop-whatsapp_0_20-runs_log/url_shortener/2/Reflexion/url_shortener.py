import time
from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

# Mock database
urls_db = {}

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	url = request.json.get('url')
	custom_alias = request.json.get('custom_alias')
	expiration_date = request.json.get('expiration_date')

	# Check if the URL is active and legitimate
	# For simplicity, we'll skip this step

	# Generate a unique shortened URL
	shortened_url = custom_alias if custom_alias else str(hash(url))

	# Save the URL to the database
	urls_db[shortened_url] = {'url': url, 'expiration_date': expiration_date, 'clicks': []}

	return jsonify({'shortened_url': shortened_url})

@app.route('/<shortened_url>', methods=['GET'])
def redirect_to_url(shortened_url):
	url_data = urls_db.get(shortened_url)

	if not url_data:
		return jsonify({'error': 'URL not found'}), 404

	# Check if the URL has expired
	if url_data['expiration_date'] and time.time() >= url_data['expiration_date']:
		return jsonify({'error': 'URL has expired'}), 410

	# Update click data
	url_data['clicks'].append({'timestamp': time.time(), 'location': 'Unknown'})

	return redirect(url_data['url'])

@app.route('/analytics/<shortened_url>', methods=['GET'])
def get_analytics(shortened_url):
	url_data = urls_db.get(shortened_url)

	if not url_data:
		return jsonify({'error': 'URL not found'}), 404

	return jsonify({'clicks': url_data['clicks']})

if __name__ == '__main__':
	app.run(debug=True)
