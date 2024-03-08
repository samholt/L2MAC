import unittest
from url_shortener import URLShortener
from database import Database


class TestURLShortenerAndDatabase(unittest.TestCase):
    def setUp(self):
        self.url_shortener = URLShortener()
        self.database = Database(':memory:')

    def test_shorten_url(self):
        original_url = 'https://example.com'
        shortened_url = self.url_shortener.shorten_url(original_url)
        self.assertEqual(len(shortened_url), 6)
        self.assertNotEqual(shortened_url, original_url)

    def test_get_original_url(self):
        original_url = 'https://example.com'
        shortened_url = self.url_shortener.shorten_url(original_url)
        self.url_shortener.url_mapping[shortened_url] = original_url
        retrieved_url = self.url_shortener.get_original_url(shortened_url)
        self.assertEqual(retrieved_url, original_url)

    def test_database_store_and_retrieve(self):
        original_url = 'https://example.com'
        shortened_url = self.url_shortener.shorten_url(original_url)
        self.database.store_url_mapping(original_url, shortened_url)
        retrieved_original_url = self.database.get_original_url(shortened_url)
        retrieved_shortened_url = self.database.get_shortened_url(original_url)
        self.assertEqual(retrieved_original_url, original_url)
        self.assertEqual(retrieved_shortened_url, shortened_url)


if __name__ == '__main__':
    unittest.main()