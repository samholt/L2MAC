import pytest
try:
	import flask
	import flask_jwt_extended
	import flask_sqlalchemy
	import flask_migrate
	def test_imports():
		assert flask
		assert flask_jwt_extended
		assert flask_sqlalchemy
		assert flask_migrate
except ImportError:
	print('Some modules are not installed.')
