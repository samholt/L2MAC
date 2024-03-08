import services
import datetime


def test_generate_short_url():
	url_shortener_service = services.URLShortenerService()

	# Create a user
	url_shortener_service.create_user('user1', 'password1')

	# Test with a valid URL
	short_url = url_shortener_service.generate_short_url('https://www.google.com', 'user1')
	assert len(short_url) == 6

	# Test with an invalid URL
	short_url = url_shortener_service.generate_short_url('invalid_url', 'user1')
	assert short_url == 'Invalid URL'

	# Test with a custom short URL
	short_url = url_shortener_service.generate_short_url('https://www.google.com', 'user1', custom_short_url='custom')
	assert short_url == 'custom'

	# Test with a custom short URL that is already in use
	short_url = url_shortener_service.generate_short_url('https://www.google.com', 'user1', custom_short_url='custom')
	assert short_url == 'Short URL already in use'

	# Test with an expiration date
	expiration_date = datetime.datetime.now() + datetime.timedelta(days=1)
	short_url = url_shortener_service.generate_short_url('https://www.google.com', 'user1', expiration_date=expiration_date)
	assert url_shortener_service.get_original_url(short_url) == 'https://www.google.com'

	# Test with an expired URL
	expiration_date = datetime.datetime.now() - datetime.timedelta(days=1)
	short_url = url_shortener_service.generate_short_url('https://www.google.com', 'user1', expiration_date=expiration_date)
	assert url_shortener_service.get_original_url(short_url) == 'URL has expired'


def test_record_click():
	url_shortener_service = services.URLShortenerService()

	# Create a user
	url_shortener_service.create_user('user1', 'password1')

	short_url = url_shortener_service.generate_short_url('https://www.google.com', 'user1')
	url_shortener_service.record_click(short_url, datetime.datetime.now(), 'USA')
	analytics = url_shortener_service.get_analytics(short_url)
	assert len(analytics['clicks']) == 1
	assert analytics['clicks'][0]['location'] == 'USA'


def test_user_management():
	url_shortener_service = services.URLShortenerService()

	# Test user creation
	message = url_shortener_service.create_user('user1', 'password1')
	assert message == 'User created successfully'

	# Test user creation with an existing username
	message = url_shortener_service.create_user('user1', 'password1')
	assert message == 'Username already taken'

	# Test user authentication
	message = url_shortener_service.authenticate_user('user1', 'password1')
	assert message == 'Authentication successful'

	# Test user authentication with an invalid password
	message = url_shortener_service.authenticate_user('user1', 'wrong_password')
	assert message == 'Invalid username or password'

	# Test user authentication with a non-existent username
	message = url_shortener_service.authenticate_user('non_existent_user', 'password1')
	assert message == 'Invalid username or password'

	# Test retrieving a user's URLs
	short_url = url_shortener_service.generate_short_url('https://www.google.com', 'user1')
	urls = url_shortener_service.get_user_urls('user1')
	assert short_url in urls


def test_admin_features():
	url_shortener_service = services.URLShortenerService()

	# Create a user
	url_shortener_service.create_user('user1', 'password1')

	# Generate a short URL
	short_url = url_shortener_service.generate_short_url('https://www.google.com', 'user1')

	# Test retrieving all URLs
	urls = url_shortener_service.get_all_urls()
	assert len(urls) == 1
	assert urls[0]['short_url'] == short_url

	# Test deleting a URL
	message = url_shortener_service.delete_url(short_url)
	assert message == 'URL deleted successfully'
	urls = url_shortener_service.get_all_urls()
	assert len(urls) == 0

	# Test deleting a user
	message = url_shortener_service.delete_user('user1')
	assert message == 'User deleted successfully'
	assert 'user1' not in url_shortener_service.user_database


