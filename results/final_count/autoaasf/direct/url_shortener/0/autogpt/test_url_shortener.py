import unittest
from url_shortener import URLShortener


class TestURLShortener(unittest.TestCase):
    def setUp(self):
        self.url_shortener = URLShortener()

    def test_generate_short_url(self):
        original_url = 'https://www.example.com'
        short_url = self.url_shortener.generate_short_url(original_url)
        self.assertTrue(short_url.startswith('https://short.url/'))

    def test_get_original_url(self):
        original_url = 'https://www.example.com'
        short_url = self.url_shortener.generate_short_url(original_url)
        retrieved_original_url = self.url_shortener.get_original_url(short_url)
        self.assertEqual(retrieved_original_url, original_url)

    def test_store_url_mapping(self):
        original_url = 'https://www.example.com'
        short_url = 'https://short.url/test'
        self.url_shortener.store_url_mapping(original_url, short_url)
        self.assertEqual(self.url_shortener.url_mapping[short_url], original_url)

    def test_generate_unique_key(self):
        key1 = self.url_shortener.generate_unique_key()
        key2 = self.url_shortener.generate_unique_key()
        self.assertNotEqual(key1, key2)


if __name__ == '__main__':
    unittest.main()