from flask import Flask, redirect, request
from models import db, URL
import string
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)

@app.route('/', methods=['POST'])
def create():
	original_url = request.json['original_url']
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	url = URL(original_url=original_url, short_url=short_url)
	db.session.add(url)
	db.session.commit()
	return {'short_url': short_url}

@app.route('/<short_url>', methods=['GET'])
def redirect_to_original(short_url):
	url = URL.query.filter_by(short_url=short_url).first()
	if url:
		url.clicks += 1
		db.session.commit()
		return redirect(url.original_url)
	else:
		return {'error': 'URL not found'}, 404

@app.route('/<short_url>/stats', methods=['GET'])
def stats(short_url):
	url = URL.query.filter_by(short_url=short_url).first()
	if url:
		return {'clicks': url.clicks}
	else:
		return {'error': 'URL not found'}, 404
