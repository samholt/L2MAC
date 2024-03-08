import unittest
from url_shortener import URLShortener


class TestURLShortener(unittest.TestCase):
    def setUp(self):
        self.url_shortener = URLShortener()

    def test_validate_url(self):
        # TODO: Implement URL validation tests
        pass

    def test_generate_short_url(self):
        short_url1 = self.url_shortener.generate_short_url()
        short_url2 = self.url_shortener.generate_short_url()
        self.assertNotEqual(short_url1, short_url2)

    def test_shorten_url(self):
        original_url = 'https://www.example.com'
        short_url = self.url_shortener.shorten_url(original_url)
        self.assertEqual(self.url_shortener.get_original_url(short_url), original_url)

    def test_get_original_url(self):
        original_url = 'https://www.example.com'
        short_url = self.url_shortener.shorten_url(original_url)
        self.assertEqual(self.url_shortener.get_original_url(short_url), original_url)
        with self.assertRaises(KeyError):
            self.url_shortener.get_original_url('invalid_short_url')


if __name__ == '__main__':
    unittest.main()