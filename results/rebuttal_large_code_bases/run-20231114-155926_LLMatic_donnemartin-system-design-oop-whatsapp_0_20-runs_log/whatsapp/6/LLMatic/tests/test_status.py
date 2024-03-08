import unittest
from app import create_app, db
from app.models import User, Status
from datetime import datetime


class StatusTestCase(unittest.TestCase):
	def setUp(self):
		self.app = create_app('testing')
		self.app_context = self.app.app_context()
		self.app_context.push()
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()
		self.app_context.pop()

	def test_post_status(self):
		u = User(username='john', password='cat')
		db.session.add(u)
		db.session.commit()
		response = self.app.test_client().post('/post_status', data=dict(username='john', content='Hello World'))
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Status posted successfully!', response.data)

	def test_view_status(self):
		u = User(username='john', password='cat')
		db.session.add(u)
		db.session.commit()
		s = Status(id=1, user=u, image='', timestamp=datetime.now(), visibility='')
		db.session.add(s)
		db.session.commit()
		response = self.app.test_client().get('/view_status/john')
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Hello World', response.data)
