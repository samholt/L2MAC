import pytest
import sys
sys.path.insert(0, '..')
from app import main, config


def test_home_route():
	client = main.app.test_client()
	response = client.get('/')
	assert response.status_code == 200
	assert response.data == b'Hello, World!'

def test_config():
	assert config.Config.SECRET_KEY is not None
	assert config.Config.SQLALCHEMY_DATABASE_URI is not None
