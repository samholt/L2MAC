import pytest
from flask import Flask
import views

app = Flask(__name__)


def test_trending():
	with app.test_request_context():
		response, status_code = views.trending()
		assert status_code == 200
		assert 'trending' in response.get_json()


def test_recommendations():
	with app.test_request_context():
		response, status_code = views.recommendations('testuser')
		assert status_code == 200
		assert 'recommendations' in response.get_json()
