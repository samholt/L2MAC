from flask import Flask, request, redirect, jsonify
from controller import URLController

app = Flask(__name__)
controller = URLController()

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	original_url = request.json.get('original_url')
	short_url = controller.create_short_url(original_url)
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	original_url = controller.get_original_url(short_url)
	if original_url:
		return redirect(original_url)
	return 'URL not found', 404

@app.route('/stats/<short_url>', methods=['GET'])
def get_stats(short_url):
	click_count = controller.get_click_stats(short_url)
	if click_count is not None:
		return jsonify({'click_count': click_count})
	return 'URL not found', 404

@app.route('/delete_expired_urls', methods=['DELETE'])
def delete_expired_urls():
	controller.delete_expired_urls()
	return 'Expired URLs deleted', 200

if __name__ == '__main__':
	app.run(debug=True)
