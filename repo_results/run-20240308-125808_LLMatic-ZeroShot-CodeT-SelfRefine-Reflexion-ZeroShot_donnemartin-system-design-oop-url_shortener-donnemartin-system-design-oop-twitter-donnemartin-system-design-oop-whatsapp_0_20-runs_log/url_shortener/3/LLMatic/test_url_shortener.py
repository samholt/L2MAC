import pytest
from url_shortener import validate_url, generate_short_link, handle_custom_link, set_expiration, get_short_link
from datetime import datetime


def test_validate_url():
	assert validate_url('https://www.google.com')
	assert not validate_url('invalid_url')


def test_generate_short_link():
	link1 = generate_short_link()
	link2 = generate_short_link()
	assert len(link1) == 6
	assert len(link2) == 6
	assert link1 != link2


def test_handle_custom_link():
	assert handle_custom_link('custom') == 'custom'
	assert len(handle_custom_link(None)) == 6


def test_set_and_get_expiration():
	short_link = generate_short_link()
	set_expiration(short_link, 1)
	assert get_short_link(short_link) == short_link
	set_expiration(short_link, -1)
	assert get_short_link(short_link) == 'This URL has expired.'
