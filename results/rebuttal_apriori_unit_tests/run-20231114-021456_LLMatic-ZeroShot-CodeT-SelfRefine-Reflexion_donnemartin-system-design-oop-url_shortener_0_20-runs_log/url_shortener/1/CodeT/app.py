from flask import Flask, request, redirect
from dataclasses import dataclass
from datetime import datetime
import string
import random

app = Flask(__name__)

# Mock database
users = {}
urls = {}

@dataclass
class User:
	username: str
	password: str
	urls: dict

@dataclass
class URL:
	original: str
	shortened: str
	expiration: datetime
	clicks: int
	click_dates: list
	click_geolocations: list

@app.route('/shorten', methods=['POST'])
def shorten_url():
	# This function will be implemented later
	pass

@app.route('/<short_url>', methods=['GET'])
def redirect_to_original(short_url):
	# This function will be implemented later
	pass

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
