import unittest
from app import create_app, db
from app.models import User, Status


class StatusStoryFeatureTestCase(unittest.TestCase):
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
		u = User(email='john@example.com')
		u.set_password('cat')
		db.session.add(u)
		db.session.commit()
		s = u.post_status('image.jpg', 'Friends')
		self.assertTrue(s is not None)

	def test_view_statuses(self):
		u1 = User(email='john@example.com')
		u1.set_password('cat')
		db.session.add(u1)
		u2 = User(email='susan@example.com')
		u2.set_password('dog')
		db.session.add(u2)
		db.session.commit()
		s1 = u1.post_status('image1.jpg', 'Friends')
		s2 = u2.post_status('image2.jpg', 'Everyone')
		statuses = u1.view_statuses()
		self.assertTrue(s1 in statuses)
		self.assertTrue(s2 not in statuses)

