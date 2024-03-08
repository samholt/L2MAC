import unittest
from app import create_app, db
from datetime import datetime, timedelta


class TestConnectivity(unittest.TestCase):

	def setUp(self):
		self.app = create_app('testing')
		self.client = self.app.test_client()
		self.app_context = self.app.app_context()
		self.app_context.push()
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()
		self.app_context.pop()

	def test_check_status(self):
		response = self.client.get('/connectivity/status')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.get_json(), {'status': 'online'})

	def test_online_status(self):
		response = self.client.get('/connectivity/online_status', query_string={'user_id': '1'})
		self.assertEqual(response.status_code, 200)
		self.assertIn('online_status', response.get_json())

	def test_queue_message(self):
		response = self.client.post('/connectivity/queue', json={'user_id': '1', 'content': 'Hello'})
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.get_json(), {'message': 'Message queued'})

	def test_queue_message_invalid(self):
		response = self.client.post('/connectivity/queue', json={'user_id': '1'})
		self.assertEqual(response.status_code, 400)
		self.assertEqual(response.get_json(), {'error': 'Invalid request'})

if __name__ == '__main__':
	unittest.main()
