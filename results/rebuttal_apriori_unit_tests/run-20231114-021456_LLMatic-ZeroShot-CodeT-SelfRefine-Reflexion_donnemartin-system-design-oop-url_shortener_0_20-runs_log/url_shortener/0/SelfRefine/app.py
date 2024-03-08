from flask import Flask, request, redirect
from dataclasses import dataclass
from datetime import datetime, timedelta
import random
import string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	password = db.Column(db.String(120), nullable=False)
	urls = db.relationship('URL', backref='user', lazy=True)

def __repr__(self):
	return f'<User {self.username}>'

class URL(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	original = db.Column(db.String(120), nullable=False)
	shortened = db.Column(db.String(120), nullable=False)
	expiration = db.Column(db.DateTime, nullable=False)
	clicks = db.Column(db.Integer, default=0)
	click_dates = db.Column(db.PickleType, nullable=True)
	click_geolocations = db.Column(db.PickleType, nullable=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

def __repr__(self):
	return f'<URL {self.shortened}>'

@app.route('/shorten', methods=['POST'])
def shorten_url():
	original_url = request.form['url']
	shortened_url = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
	new_url = URL(original=original_url, shortened=shortened_url, expiration=datetime.now() + timedelta(days=1))
	db.session.add(new_url)
	db.session.commit()
	return {'shortened_url': shortened_url}

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	url = URL.query.filter_by(shortened=short_url).first()
	if url and url.expiration > datetime.now():
		return redirect(url.original)
	else:
		return {'error': 'URL not found or expired'}, 404

@app.route('/analytics', methods=['GET'])
def get_analytics():
	# This function will be implemented later
	pass

@app.route('/user', methods=['POST'])
def create_user():
	# This function will be implemented later
	pass

@app.route('/user/<username>', methods=['GET', 'PUT', 'DELETE'])
def manage_user(username):
	# This function will be implemented later
	pass

@app.route('/admin', methods=['POST'])
def create_admin():
	# This function will be implemented later
	pass

@app.route('/admin/<username>', methods=['GET', 'DELETE'])
def manage_admin(username):
	# This function will be implemented later
	pass

if __name__ == '__main__':
	app.run(debug=True)
