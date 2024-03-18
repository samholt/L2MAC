from flask import render_template, redirect
from app import app
from services import get_original_url

@app.route('/')
def home():
	return 'Welcome to the URL Shortener!'

@app.route('/<string:short_url>')
def redirect_to_original(short_url):
	original_url = get_original_url(short_url)
	if original_url is not None:
		return redirect(original_url)
	else:
		return 'URL not found', 404
