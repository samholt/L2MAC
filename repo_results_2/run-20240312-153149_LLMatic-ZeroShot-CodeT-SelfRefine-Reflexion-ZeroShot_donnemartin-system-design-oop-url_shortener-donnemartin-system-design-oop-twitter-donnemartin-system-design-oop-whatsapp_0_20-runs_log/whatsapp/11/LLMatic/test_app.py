import app
import unittest
import json
import time

# Existing tests...

class TestConnectivity(unittest.TestCase):

	def setUp(self):
		self.app = app.app.test_client()
		app.users = {'1': {'groups': [], 'statuses': [], 'online': True}, '2': {'groups': [], 'statuses': [], 'online': False}}
		app.messages = {'1': {'2': []}, '2': {'1': []}}
		app.offline_messages = {'2': [{'sender_id': '1', 'message': 'Hello'}]}

	def test_send_message(self):
		response = self.app.post('/send_message', data=json.dumps({'sender_id': '1', 'receiver_id': '2', 'message': 'Hello'}), content_type='application/json')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json['message'], 'User is offline. Message queued.')

	def test_set_online_status(self):
		response = self.app.post('/set_online_status', data=json.dumps({'user_id': '2', 'online_status': True}), content_type='application/json')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json['message'], 'Online status set successfully.')
		self.assertEqual(len(app.offline_messages['2']), 0)
		self.assertEqual(len(app.messages['1']['2']), 1)

	def test_get_online_status(self):
		response = self.app.get('/get_online_status', query_string={'user_id': '2'})
		self.assertEqual(response.status_code, 200)
		self.assertIn('online_status', response.json)

# Existing tests...

if __name__ == '__main__':
	unittest.main()
