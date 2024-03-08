from flask import Flask, request, redirect
from utils import shorten_url, get_original_url, update_analytics, get_analytics

app = Flask(__name__)

@app.route('/shorten_url', methods=['POST'])
def shorten_url_route():
	url = request.json.get('url')
	shortened_url = shorten_url(url)
	return {'shortened_url': shortened_url}

@app.route('/<short_url>', methods=['GET'])
def redirect_to_original(short_url):
	original_url = get_original_url(short_url)
	if original_url is not None:
		update_analytics(short_url, request.headers.get('X-Forwarded-For', request.remote_addr))
		return redirect(original_url)
	else:
		return {'error': 'URL not found'}, 404

@app.route('/analytics/<short_url>', methods=['GET'])
def get_url_analytics(short_url):
	analytics = get_analytics(short_url)
	if analytics is not None:
		return analytics
	else:
		return {'error': 'Analytics not found'}, 404
