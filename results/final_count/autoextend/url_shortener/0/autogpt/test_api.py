import unittest
import json
from api import app


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_shorten_url(self):
        response = self.app.post('/shorten', json={'url': 'https://example.com'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('shortened_url', data)
        self.assertEqual(len(data['shortened_url']), 6)

    def test_redirect_to_original(self):
        response = self.app.post('/shorten', json={'url': 'https://example.com'})
        data = json.loads(response.data)
        shortened_url = data['shortened_url']
        redirect_response = self.app.get(f'/{shortened_url}')
        self.assertEqual(redirect_response.status_code, 302)
        self.assertEqual(redirect_response.location, 'https://example.com')


if __name__ == '__main__':
    unittest.main()