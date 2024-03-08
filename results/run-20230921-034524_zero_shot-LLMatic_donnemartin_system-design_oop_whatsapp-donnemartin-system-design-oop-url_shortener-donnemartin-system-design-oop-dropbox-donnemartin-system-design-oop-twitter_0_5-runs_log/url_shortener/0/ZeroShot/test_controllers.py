from controllers import create_url, get_original_url, get_clicks, delete_expired_urls
from models import db, Url


def test_create_url():
	url = create_url('https://example.com')
	assert url.original_url == 'https://example.com'
	assert len(url.short_url) == 6


def test_get_original_url():
	url = create_url('https://example.com')
	original_url = get_original_url(url.short_url)
	assert original_url == 'https://example.com'


def test_get_clicks():
	url = create_url('https://example.com')
	clicks = get_clicks(url.short_url)
	assert clicks == 0


def test_delete_expired_urls():
	url = Url(original_url='https://example.com', short_url='abcdef', expires_on=datetime.now() - timedelta(days=1))
	db.session.add(url)
	db.session.commit()
	delete_expired_urls()
	assert Url.query.get(url.id) is None
