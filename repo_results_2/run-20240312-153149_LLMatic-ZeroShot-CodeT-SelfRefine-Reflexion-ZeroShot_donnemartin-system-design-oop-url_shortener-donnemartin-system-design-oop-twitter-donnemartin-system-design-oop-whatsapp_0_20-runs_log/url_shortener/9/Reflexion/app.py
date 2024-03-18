from flask import Flask, request, redirect
from dataclasses import dataclass
from datetime import datetime
import geopy

app = Flask(__name__)

# Mock database
urls = {}
users = {}

@dataclass
class URL:
	original: str
	short: str
	user: str
	clicks: int
	created_at: datetime
	expires_at: datetime

@app.route('/shorten', methods=['POST'])
def shorten_url():
	# TODO: Implement URL shortening

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	# TODO: Implement URL redirection

@app.route('/analytics', methods=['GET'])
def view_analytics():
	# TODO: Implement analytics viewing

@app.route('/admin', methods=['GET', 'POST'])
def admin_dashboard():
	# TODO: Implement admin dashboard

@app.route('/expire', methods=['POST'])
def set_expiration():
	# TODO: Implement URL expiration

if __name__ == '__main__':
	app.run(debug=True)
