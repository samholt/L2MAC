import unittest
from url_shortener import URLShortener, Redirector
import datetime


class TestURLShortener(unittest.TestCase):
    def setUp(self):
        self.url_shortener = URLShortener()
        self.redirector = Redirector(self.url_shortener)

    def test_generate_short_url(self):
        long_url = 'https://www.example.com'
        short_url = self.url_shortener.generate_short_url(long_url)
        self.assertIsNotNone(short_url)
        self.assertNotEqual(long_url, short_url)

    def test_custom_alias(self):
        long_url = 'https://www.example.com'
        custom_alias = 'custom'
        short_url = self.url_shortener.generate_short_url(long_url, custom_alias=custom_alias)
        self.assertEqual(short_url, custom_alias)

    def test_get_long_url(self):
        long_url = 'https://www.example.com'
        short_url = self.url_shortener.generate_short_url(long_url)
        retrieved_long_url = self.url_shortener.get_long_url(short_url)
        self.assertEqual(long_url, retrieved_long_url)

    def test_redirect(self):
        long_url = 'https://www.example.com'
        short_url = self.url_shortener.generate_short_url(long_url)
        redirected_url = self.redirector.redirect(short_url)
        self.assertEqual(long_url, redirected_url)

    def test_redirect_not_found(self):
        short_url = 'nonexistent'
        redirected_url = self.redirector.redirect(short_url)
        self.assertEqual('URL not found', redirected_url)

    def test_click_stats(self):
        long_url = 'https://www.example.com'
        short_url = self.url_shortener.generate_short_url(long_url)
        self.redirector.redirect(short_url)
        click_stats = self.url_shortener.get_click_stats(short_url)
        self.assertEqual(1, click_stats)

    def test_delete_expired_urls(self):
        long_url = 'https://www.example.com'
        expiration_date = datetime.datetime.now() - datetime.timedelta(minutes=1)
        short_url = self.url_shortener.generate_short_url(long_url, expiration_date=expiration_date)
        self.url_shortener.delete_expired_urls()
        retrieved_long_url = self.url_shortener.get_long_url(short_url)
        self.assertIsNone(retrieved_long_url)


if __name__ == '__main__':
    unittest.main()
