import unittest
import app
import mock_db

class TestApp(unittest.TestCase):
	def setUp(self):
		app.app.config['TESTING'] = True
		self.app = app.app.test_client()
		self.db = mock_db.MockDB()

	def test_send_message(self):
		with app.app.app_context():
			app.g.db = self.db
			response = self.app.post('/send_message', json={'message_id': '1', 'text': 'Hello'})
			self.assertEqual(response.status_code, 200)
			self.assertEqual(response.get_json(), {'status': 'message sent'})
			self.db.set_online(False)
			response = self.app.post('/send_message', json={'message_id': '2', 'text': 'Hi'})
			self.assertEqual(response.status_code, 200)
			self.assertEqual(response.get_json(), {'status': 'message queued'})
			self.db.set_online(True)
			response = self.app.post('/send_message', json={'message_id': '3', 'text': 'Hey'})
			self.assertEqual(response.status_code, 200)
			self.assertEqual(response.get_json(), {'status': 'message sent'})
			self.assertEqual(self.db.retrieve('2'), {'text': 'Hi'})
			self.assertEqual(self.db.retrieve('3'), {'text': 'Hey'})
