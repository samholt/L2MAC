import string
import random
from datetime import datetime, timedelta
from models import db, Url


def generate_short_url():
	characters = string.ascii_letters + string.digits
	short_url = ''.join(random.choice(characters) for _ in range(6))
	return short_url


def create_url(original_url, custom_url=None):
	short_url = generate_short_url()
	url = Url(original_url=original_url, short_url=short_url, custom_url=custom_url)
	db.session.add(url)
	db.session.commit()
	return url


def get_original_url(short_url):
	url = Url.query.filter_by(short_url=short_url).first()
	if url:
		url.clicks += 1
		db.session.commit()
		return url.original_url


def get_clicks(short_url):
	url = Url.query.filter_by(short_url=short_url).first()
	if url:
		return url.clicks


def delete_expired_urls():
	expired_urls = Url.query.filter(Url.expires_on < datetime.now()).all()
	for url in expired_urls:
		db.session.delete(url)
	db.session.commit()
