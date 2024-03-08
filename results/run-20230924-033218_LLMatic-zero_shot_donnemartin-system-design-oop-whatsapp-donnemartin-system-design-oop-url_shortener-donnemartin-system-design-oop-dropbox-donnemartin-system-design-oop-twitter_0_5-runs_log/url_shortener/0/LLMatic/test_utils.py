import utils


def test_validate_url():
	assert utils.validate_url('https://www.google.com') == True
	assert utils.validate_url('invalid_url') == False


def test_generate_shortened_url():
	url = 'https://www.google.com'
	shortened_url = utils.generate_shortened_url(url)
	assert len(shortened_url) == 6
	assert utils.validate_url(shortened_url) == False

	custom = 'custom'
	shortened_url = utils.generate_shortened_url(url, custom)
	assert shortened_url == custom


def test_gather_click_data():
	click_event = {'time': '2022-01-01T00:00:00', 'location': 'USA'}
	click = utils.gather_click_data(click_event)
	assert click.click_time == '2022-01-01T00:00:00'
	assert click.click_location == 'USA'
