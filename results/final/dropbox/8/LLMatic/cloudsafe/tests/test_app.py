import pytest
from cloudsafe.app import create_app

def test_create_app():
	app = create_app()
	assert app is not None
	assert app.name == 'cloudsafe.app'
	assert 'user' in app.blueprints
	assert 'file' in app.blueprints
	assert 'security' in app.blueprints
