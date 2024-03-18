import pytest
import app
import datetime

# Test URL validation
def test_validate_url():
	assert app.validate_url('https://www.google.com') == True
	assert app.validate_url('invalid_url') == False

# Test URL shortening
def test_shorten_url():
	response = app.shorten_url()
	assert response.status_code == 200
	assert 'short_url' in response.get_json()

# Test URL redirection
def test_redirect_url():
	response = app.redirect_url('invalid_url')
	assert response.status_code == 404

# Test analytics
def test_get_analytics():
	response = app.get_analytics()
	assert response.status_code == 200

# Test user account creation
def test_create_user():
	response = app.create_user()
	assert response.status_code == 201

# Test admin dashboard
def test_admin_dashboard():
	response = app.admin_dashboard()
	assert response.status_code == 200
