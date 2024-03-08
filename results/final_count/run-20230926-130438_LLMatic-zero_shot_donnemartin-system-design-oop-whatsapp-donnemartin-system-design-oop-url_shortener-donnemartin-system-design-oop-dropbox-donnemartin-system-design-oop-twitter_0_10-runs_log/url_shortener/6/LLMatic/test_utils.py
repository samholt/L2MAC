import utils


def test_generate_short_url():
	short_url = utils.generate_short_url()
	assert len(short_url) == 6
	assert short_url.isalnum()


def test_check_url_availability():
	utils.DATABASE.clear()
	assert utils.check_url_availability('test')
	utils.DATABASE['test'] = 'http://example.com'
	assert not utils.check_url_availability('test')


def test_check_url_validity():
	assert utils.check_url_validity('http://example.com')
	assert not utils.check_url_validity('http://invalid.url')


def test_shorten_url():
	utils.DATABASE.clear()
	assert utils.shorten_url('http://invalid.url') == 'Invalid URL'
	assert utils.shorten_url('http://example.com', 'test') == 'test'
	assert utils.shorten_url('http://example.com', 'test') == 'Custom short URL is not available'
	short_url = utils.shorten_url('http://example.com')
	assert len(short_url) == 6
	assert short_url.isalnum()
	assert utils.DATABASE[short_url] == 'http://example.com'
