from flask import Flask, request, redirect
from dataclasses import dataclass
from datetime import datetime
import pytz
import string
import random
import requests

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
def shorten():
	# TODO: Implement URL shortening
	pass

@app.route('/<short_url>', methods=['GET'])
def redirect(short_url):
	# TODO: Implement URL redirection
	pass

@app.route('/analytics', methods=['GET'])
def analytics():
	# TODO: Implement analytics retrieval
	pass

@app.route('/user', methods=['POST'])
def create_user():
	# TODO: Implement user account creation
	pass

@app.route('/user/<username>', methods=['GET', 'PUT', 'DELETE'])
def user(username):
	# TODO: Implement user account retrieval, update, and deletion
	pass

@app.route('/admin', methods=['POST'])
def create_admin():
	# TODO: Implement admin account creation
	pass

@app.route('/admin/<username>', methods=['GET', 'PUT', 'DELETE'])
def admin(username):
	# TODO: Implement admin account retrieval, update, and deletion
	pass

if __name__ == '__main__':
	app.run(debug=True)
