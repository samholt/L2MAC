from flask import Flask, redirect, request
from controllers import create_url, get_original_url, get_clicks, delete_expired_urls


app = Flask(__name__)


@app.route('/', methods=['POST'])

def create_short_url():
	original_url = request.form['original_url']
	custom_url = request.form.get('custom_url')
	url = create_url(original_url, custom_url)
	return {'short_url': url.short_url, 'custom_url': url.custom_url}


@app.route('/<short_url>')

def redirect_to_original(short_url):
	original_url = get_original_url(short_url)
	if original_url:
		return redirect(original_url)
	else:
		return {'error': 'URL not found'}, 404


@app.route('/<short_url>/clicks')

def show_clicks(short_url):
	clicks = get_clicks(short_url)
	if clicks is not None:
		return {'clicks': clicks}
	else:
		return {'error': 'URL not found'}, 404


@app.route('/delete_expired')

def delete_expired():
	delete_expired_urls()
	return {'status': 'success'}
