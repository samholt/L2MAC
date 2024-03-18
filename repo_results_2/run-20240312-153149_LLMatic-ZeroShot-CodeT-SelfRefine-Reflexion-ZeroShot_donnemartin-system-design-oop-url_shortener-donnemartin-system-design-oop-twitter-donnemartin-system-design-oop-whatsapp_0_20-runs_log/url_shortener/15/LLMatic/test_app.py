import app
import unittest


class TestApp(unittest.TestCase):

	def setUp(self):
		app.app.testing = True
		self.app = app.app.test_client()

	def test_home(self):
		response = self.app.get('/')
		self.assertEqual(response.data, b'Hello, World!')

	def test_shorten_url(self):
		response = self.app.post('/shorten_url', json={'url': 'https://www.google.com'})
		self.assertEqual(len(response.get_json()['short_url']), 10)

	def test_create_account(self):
		response = self.app.post('/create_account', json={'username': 'test_user'})
		self.assertEqual(response.get_json()['message'], 'Account created successfully.')

	def test_view_urls(self):
		self.app.post('/create_account', json={'username': 'test_user'})
		response = self.app.post('/view_urls', json={'username': 'test_user'})
		self.assertEqual(response.get_json(), {})

	def test_edit_url(self):
		self.app.post('/create_account', json={'username': 'test_user'})
		response = self.app.post('/shorten_url', json={'url': 'https://www.google.com'})
		short_url = response.get_json()['short_url']
		self.app.post('/edit_url', json={'username': 'test_user', 'old_url': short_url, 'new_url': 'https://www.example.com'})
		response = self.app.post('/view_urls', json={'username': 'test_user'})
		self.assertEqual('https://www.example.com' in response.get_json().values(), True)

	def test_delete_url(self):
		self.app.post('/create_account', json={'username': 'test_user'})
		response = self.app.post('/shorten_url', json={'url': 'https://www.google.com'})
		short_url = response.get_json()['short_url']
		self.app.post('/delete_url', json={'username': 'test_user', 'url': short_url})
		response = self.app.post('/view_urls', json={'username': 'test_user'})
		self.assertEqual(short_url in response.get_json().values(), False)

	def test_view_statistics(self):
		response = self.app.post('/shorten_url', json={'url': 'https://www.google.com'})
		short_url = response.get_json()['short_url']
		response = self.app.post('/view_statistics', json={'short_url': short_url})
		self.assertEqual(response.get_json(), None)

if __name__ == '__main__':
	unittest.main()
