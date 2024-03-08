import unittest
from app import create_app, db
from app.models import User, Group


class GroupChatsTestCase(unittest.TestCase):
	def setUp(self):
		self.app = create_app('testing')
		self.app_context = self.app.app_context()
		self.app_context.push()
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()
		self.app_context.pop()

	def test_create_group(self):
		u = User(email='john@example.com')
		u.set_password('cat')
		db.session.add(u)
		db.session.commit()
		g = u.create_group('Test Group', 'default.jpg')
		self.assertIsNotNone(g)
		self.assertEqual(g.name, 'Test Group')
		self.assertEqual(g.picture, 'default.jpg')
		self.assertEqual(g.admin, u)

	def test_join_group(self):
		u1 = User(email='john@example.com')
		u1.set_password('cat')
		u2 = User(email='susan@example.com')
		u2.set_password('dog')
		db.session.add_all([u1, u2])
		db.session.commit()
		g = u1.create_group('Test Group', 'default.jpg')
		u2.join_group(g)
		self.assertIn(u2, g.members)

	def test_leave_group(self):
		u1 = User(email='john@example.com')
		u1.set_password('cat')
		u2 = User(email='susan@example.com')
		u2.set_password('dog')
		db.session.add_all([u1, u2])
		db.session.commit()
		g = u1.create_group('Test Group', 'default.jpg')
		u2.join_group(g)
		u2.leave_group(g)
		self.assertNotIn(u2, g.members)


if __name__ == '__main__':
	unittest.main(verbosity=2)
