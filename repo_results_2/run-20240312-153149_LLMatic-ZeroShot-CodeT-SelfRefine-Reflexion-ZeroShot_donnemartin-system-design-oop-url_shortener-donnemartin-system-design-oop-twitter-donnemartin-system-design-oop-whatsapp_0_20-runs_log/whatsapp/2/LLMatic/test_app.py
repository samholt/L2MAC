import pytest
from app import app, users
from flask import template_rendered
from contextlib import contextmanager

@contextmanager
def captured_templates(app):
	recorded = []
	def record(sender, template, context, **extra):
		recorded.append((template, context))
	template_rendered.connect(record, app)
	try:
		yield recorded
	finally:
		template_rendered.disconnect(record, app)

def test_home_route():
	with app.test_client() as c:
		with captured_templates(app) as templates:
			response = c.get('/')
			assert response.status_code == 200
			template, context = templates[0]
			assert template.name == 'chat.html'

def test_user_route():
	with app.test_client() as c:
		response = c.post('/user/testuser', json={'online': False})
		assert response.status_code == 200
		assert users['testuser']['online'] == False

def test_message_route():
	with app.test_client() as c:
		response = c.post('/message/testuser', json={'message': 'Hello'})
		assert response.status_code == 200
		assert 'Hello' in users['testuser']['queue']
