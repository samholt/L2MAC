import pytest
from flask import template_rendered
from contextlib import contextmanager
from app import app

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


def test_templates():
	with captured_templates(app) as templates:
		app.test_client().get('/register')
		template, context = templates[0]
		assert template.name == 'register.html'
		app.test_client().get('/login')
		template, context = templates[1]
		assert template.name == 'login.html'
		app.test_client().get('/book_club')
		template, context = templates[2]
		assert template.name == 'book_club.html'
		app.test_client().get('/meeting')
		template, context = templates[3]
		assert template.name == 'meeting.html'
		app.test_client().get('/forum')
		template, context = templates[4]
		assert template.name == 'forum.html'
		app.test_client().get('/profile')
		template, context = templates[5]
		assert template.name == 'profile.html'
		app.test_client().get('/admin')
		template, context = templates[6]
		assert template.name == 'admin.html'
