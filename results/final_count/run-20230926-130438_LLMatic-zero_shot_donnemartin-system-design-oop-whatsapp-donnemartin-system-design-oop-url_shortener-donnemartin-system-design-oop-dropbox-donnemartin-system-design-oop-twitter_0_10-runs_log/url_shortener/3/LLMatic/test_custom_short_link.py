import pytest
import utils


def test_generate_short_url_with_custom_link():
	custom_short_url = 'custom'
	short_url = utils.generate_short_url(custom_short_url=custom_short_url)
	assert short_url == custom_short_url


def test_generate_short_url_without_custom_link():
	short_url = utils.generate_short_url()
	assert len(short_url) == 6

