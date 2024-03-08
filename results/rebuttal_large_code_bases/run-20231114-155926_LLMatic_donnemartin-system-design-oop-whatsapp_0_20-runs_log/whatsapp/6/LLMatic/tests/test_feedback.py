import unittest
from app import create_app, db
from app.models import Feedback


class FeedbackTestCase(unittest.TestCase):
	def setUp(self):
		self.app = create_app('testing')
		self.app_context = self.app.app_context()
		self.app_context.push()
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()
		self.app_context.pop()

	def test_feedback_creation(self):
		feedback = Feedback(user_id=1, feedback='Test feedback')
		db.session.add(feedback)
		db.session.commit()
		self.assertEqual(Feedback.query.get(1).feedback, 'Test feedback')

if __name__ == '__main__':
	unittest.main()
