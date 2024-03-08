import unittest
import json
from api_error_handling import app


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_shorten_url(self):
        response = self.app.post('/shorten', json={'original_url': 'https://www.example.com'})
        self.assertEqual(response.status_code, 200)
        short_url = json.loads(response.data)['short_url']
        self.assertIsNotNone(short_url)

    def test_get_original_url(self):
        response = self.app.post('/shorten', json={'original_url': 'https://www.example.com'})
        short_url = json.loads(response.data)['short_url']
        response = self.app.get(f'/{short_url}')
        self.assertEqual(response.status_code, 200)
        original_url = json.loads(response.data)['original_url']
        self.assertEqual(original_url, 'https://www.example.com')

    def test_invalid_short_url(self):
        response = self.app.get('/invalid_short_url')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()