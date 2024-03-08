from models import db, URL
from datetime import datetime
import string
import random

class URLController:
	@staticmethod
	def create_short_url(long_url, short_url=None):
		if not short_url:
			short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
		url = URL(long_url=long_url, short_url=short_url)
		db.session.add(url)
		db.session.commit()
		return short_url

	@staticmethod
	def get_long_url(short_url):
		url = URL.query.filter_by(short_url=short_url).first()
		if url and (not url.expires_at or url.expires_at > datetime.utcnow()):
			url.click_count += 1
			db.session.commit()
			return url.long_url

	@staticmethod
	def get_click_stats(short_url):
		url = URL.query.filter_by(short_url=short_url).first()
		if url:
			return {'click_count': url.click_count}

	@staticmethod
	def delete_expired_urls():
		expired_urls = URL.query.filter(URL.expires_at < datetime.utcnow()).all()
		for url in expired_urls:
			db.session.delete(url)
		db.session.commit()
