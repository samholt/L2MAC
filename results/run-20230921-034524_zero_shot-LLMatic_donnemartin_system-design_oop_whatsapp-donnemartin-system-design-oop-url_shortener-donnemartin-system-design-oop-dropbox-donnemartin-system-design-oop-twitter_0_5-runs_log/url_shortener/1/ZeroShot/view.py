from flask import Flask, redirect, request
from controller import URLController


app = Flask(__name__)
controller = URLController()


@app.route('/create', methods=['POST'])
def create_url():
	original_url = request.form.get('original_url')
	custom_short_url = request.form.get('custom_short_url')
	short_url = controller.create_url(original_url, custom_short_url)
	return {'short_url': short_url}


@app.route('/<short_url>', methods=['GET'])
def redirect_to_original_url(short_url):
	original_url = controller.get_original_url(short_url)
	if original_url:
		return redirect(original_url)
	return {'error': 'URL not found or expired'}


@app.route('/delete_expired', methods=['DELETE'])
def delete_expired_urls():
	controller.delete_expired_urls()
	return {'status': 'success'}

