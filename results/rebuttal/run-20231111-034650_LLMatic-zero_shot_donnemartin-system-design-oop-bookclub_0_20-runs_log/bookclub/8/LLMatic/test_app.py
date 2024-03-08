import app
import unittest


class FlaskTestCase(unittest.TestCase):

	def setUp(self):
		self.app = app.app.test_client()
		self.app.testing = True 

	def test_create_book_club(self):
		result = self.app.post('/create_book_club', data=dict(name='test_club', description='This is a test club', is_private='False', admin='test_admin'), follow_redirects=True)
		self.assertEqual(result.status_code, 200)
		self.assertIn(b'test_club', result.data)

	def test_schedule_meeting(self):
		result = self.app.post('/schedule_meeting/test_club', data=dict(date='2022-12-31', time='12:00', book='Test Book'), follow_redirects=True)
		self.assertEqual(result.status_code, 200)
		self.assertIn(b'test_club', result.data)

	def test_upcoming_meetings(self):
		result = self.app.get('/upcoming_meetings/test_club', follow_redirects=True)
		self.assertEqual(result.status_code, 200)
		self.assertIn(b'Upcoming Meetings', result.data)

	def test_send_reminders(self):
		result = self.app.get('/send_reminders/test_club', follow_redirects=True)
		self.assertEqual(result.status_code, 200)
		self.assertIn(b'test_club', result.data)

if __name__ == '__main__':
	unittest.main()

