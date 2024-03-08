from views import app
from models import db, Url


def test_create_short_url():
	response = app.test_client().post('/', data={'original_url': 'https://example.com'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()


def test_redirect_to_original():
	url = Url(original_url='https://example.com', short_url='abcdef')
	db.session.add(url)
	db.session.commit()
	response = app.test_client().get('/abcdef')
	assert response.status_code == 302


def test_show_clicks():
	url = Url(original_url='https://example.com', short_url='abcdef')
	db.session.add(url)
	db.session.commit()
	response = app.test_client().get('/abcdef/clicks')
	assert response.status_code == 200
	assert response.get_json()['clicks'] == 0


def test_delete_expired():
	response = app.test_client().get('/delete_expired')
	assert response.status_code == 200
	assert response.get_json()['status'] == 'success'
