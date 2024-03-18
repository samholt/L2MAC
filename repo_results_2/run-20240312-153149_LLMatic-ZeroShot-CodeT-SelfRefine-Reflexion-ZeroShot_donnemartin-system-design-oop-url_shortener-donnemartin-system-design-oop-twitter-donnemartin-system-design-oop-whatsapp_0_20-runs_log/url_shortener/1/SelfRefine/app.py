from flask import Flask, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime, timedelta
import requests
import string
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class URL(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	original = db.Column(db.String(500), nullable=False)
	shortened = db.Column(db.String(50), unique=True, nullable=False)
	user = db.Column(db.String(50), nullable=False)
	clicks = db.Column(db.Integer, default=0)
	expiration = db.Column(db.DateTime, nullable=False)

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	short_url = data.get('short')
	user = data.get('user')
	expiration = data.get('expiration')

	# Validate URL
	try:
		response = requests.get(original_url)
		response.raise_for_status()
	except (requests.RequestException, ValueError):
		return jsonify({'error': 'Invalid URL'}), 400

	# Generate a unique short URL if not provided
	if not short_url:
		while True:
			short_url = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
			if not URL.query.filter_by(shortened=short_url).first():
				break

	# Check if short URL is available
	if URL.query.filter_by(shortened=short_url).first():
		return jsonify({'error': 'Short URL already in use'}), 400

	# Set a default expiration date if not provided
	if not expiration:
		expiration = (datetime.now() + timedelta(days=30)).isoformat()

	# Create URL object and store in DB
	url = URL(original=original_url, shortened=short_url, user=user, clicks=0, expiration=datetime.fromisoformat(expiration))
	db.session.add(url)
	db.session.commit()

	return jsonify({'message': 'URL shortened successfully', 'short_url': short_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = URL.query.filter_by(shortened=short_url).first()
	if not url or url.expiration < datetime.now():
		return jsonify({'error': 'URL not found or expired'}), 404

	# Record click
	url.clicks += 1
	db.session.commit()

	return redirect(url.original, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	data = request.get_json()
	user = data.get('user')

	# Get all URLs for user
	urls = URL.query.filter_by(user=user).all()

	# Prepare analytics data
	analytics = []
	for url in urls:
		analytics.append({
			'original': url.original,
			'shortened': url.shortened,
			'clicks': url.clicks,
			'expiration': url.expiration.isoformat()
		})

	return jsonify(analytics), 200

if __name__ == '__main__':
	app.run(debug=True)
