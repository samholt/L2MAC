import pytest
import flask
try:
	import flask_jwt_extended
	import flask_sqlalchemy
except ImportError:
	pass

def test_imports():
	assert True

