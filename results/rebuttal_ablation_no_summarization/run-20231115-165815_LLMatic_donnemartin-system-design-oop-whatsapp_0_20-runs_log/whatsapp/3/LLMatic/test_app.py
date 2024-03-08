import app
import unittest


class TestApp(unittest.TestCase):

	def setUp(self):
		app.app.testing = True
		self.app = app.app.test_client()

	def test_message_queue(self):
		response = self.app.post('/send_message', data={'sender': 'test1@test.com', 'receiver': 'test3@test.com', 'content': 'Hello'})
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.get_json(), {'message': 'User is offline. Message queued.'})

	def test_online_status(self):
		response = self.app.get('/online_status', query_string={'user_id': 'test1@test.com'})
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.get_json(), {'online': False})

if __name__ == '__main__':
	unittest.main()
