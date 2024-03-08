from flask import Flask, redirect, request
from models import db, URL
from controllers import URLController

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)

@app.route('/<short_url>', methods=['GET'])
def redirect_to_long_url(short_url):
	url = URLController.get_long_url(short_url)
	if url:
		return redirect(url)
	else:
		return 'URL not found', 404

@app.route('/create', methods=['POST'])
def create_short_url():
	long_url = request.json.get('long_url')
	short_url = request.json.get('short_url')
	url = URLController.create_short_url(long_url, short_url)
	if url:
		return {'short_url': url}
	else:
		return 'Failed to create short URL', 400

@app.route('/stats/<short_url>', methods=['GET'])
def get_click_stats(short_url):
	stats = URLController.get_click_stats(short_url)
	if stats:
		return stats
	else:
		return 'URL not found', 404

if __name__ == '__main__':
	app.run(debug=True)
