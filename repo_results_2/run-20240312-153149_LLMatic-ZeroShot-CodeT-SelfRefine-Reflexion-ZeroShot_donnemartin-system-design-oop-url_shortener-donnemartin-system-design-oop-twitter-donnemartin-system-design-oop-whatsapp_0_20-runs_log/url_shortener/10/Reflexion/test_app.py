import pytest
import app
from unittest.mock import patch

@patch('app.get_location', return_value='Test location')
def test_shorten_url(mock_get_location):
	response = app.shorten_url()
	assert 'short_url' in response

@patch('app.get_location', return_value='Test location')
def test_redirect_to_original(mock_get_location):
	short_url = list(app.DB.keys())[0]
	response = app.redirect_to_original(short_url)
	assert response.status_code == 302

@patch('app.get_location', return_value='Test location')
def test_get_analytics(mock_get_location):
	short_url = list(app.DB.keys())[0]
	response = app.get_analytics(short_url)
	assert 'original_url' in response
	assert 'clicks' in response
	assert 'click_data' in response
