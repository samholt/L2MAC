import views
import utils
import models
import datetime


def test_redirect_to_url():
	user = models.User('test', 'test')
	url = models.URL('http://test.com', 'test', user, datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=1))
	user.urls.append(url)
	utils.save_user(user)
	response = views.app.test_client().get('/test')
	assert response.status_code == 302
	assert response.location == 'http://test.com'

	url.expiration_date = datetime.datetime.now() - datetime.timedelta(days=1)
	response = views.app.test_client().get('/test')
	assert response.status_code == 400
	assert response.get_json() == {'error': 'URL has expired'}
