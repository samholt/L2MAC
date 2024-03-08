import utils


def test_validate_url():
	assert utils.validate_url('https://www.google.com') == True
	assert utils.validate_url('https://www.nonexistentwebsite123456.com') == False


def test_generate_short_link():
	link1 = utils.generate_short_link()
	link2 = utils.generate_short_link()
	assert len(link1) == 6
	assert len(link2) == 6
	assert link1 != link2


def test_handle_custom_short_link():
	existing_links = ['abc123', 'def456']
	assert utils.handle_custom_short_link('abc123', existing_links) == {'error': 'Requested short link is already in use.'}
	assert utils.handle_custom_short_link('ghi789', existing_links) == 'ghi789'
