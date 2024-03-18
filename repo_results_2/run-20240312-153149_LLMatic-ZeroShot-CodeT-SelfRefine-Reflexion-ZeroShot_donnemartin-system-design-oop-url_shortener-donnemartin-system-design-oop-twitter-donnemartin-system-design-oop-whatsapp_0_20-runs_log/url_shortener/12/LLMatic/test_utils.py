import utils


def test_validate_url():
	assert utils.validate_url('https://www.google.com') == True
	assert utils.validate_url('invalid_url') == False


def test_generate_short_link():
	short_link = utils.generate_short_link()
	assert len(short_link) == 6
	assert short_link.isalnum() == True


def test_check_availability():
	url_db = {'short1': 'https://www.google.com'}
	assert utils.check_availability('short1', url_db) == False
	assert utils.check_availability('short2', url_db) == True
