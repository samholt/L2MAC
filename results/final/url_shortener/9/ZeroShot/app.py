from flask import Flask, request, redirect, jsonify
import requests
from geolite2 import geolite2
from datetime import datetime
import string
import random

app = Flask(__name__)

# Mock database
users = {}
urls = {}

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	# Your code here
	pass

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	# Your code here
	pass

@app.route('/analytics', methods=['GET'])
def get_analytics():
	# Your code here
	pass

@app.route('/user', methods=['POST'])
def create_user():
	# Your code here
	pass

@app.route('/user/<username>', methods=['GET', 'PUT', 'DELETE'])
def manage_user(username):
	# Your code here
	pass

@app.route('/admin', methods=['GET', 'DELETE'])
def admin_dashboard():
	# Your code here
	pass

if __name__ == '__main__':
	app.run(debug=True)
