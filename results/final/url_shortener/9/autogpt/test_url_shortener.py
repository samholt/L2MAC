import unittest
from datetime import datetime, timedelta
from url_shortener_controller import URLShortenerController


class TestURLShortener(unittest.TestCase):
    def setUp(self):
        self.controller = URLShortenerController()

    def test_create_short_url(self):
        short_url = self.controller.create_short_url('https://example.com')
        self.assertIsNotNone(short_url)

    def test_custom_short_url(self):
        self.controller.create_short_url('https://example.com', custom_alias='custom')
        self.assertEqual(self.controller.redirect_to_long_url('custom'), 'https://example.com')

    def test_click_tracking(self):
        self.controller.create_short_url('https://example.com', custom_alias='clicktest')
        self.assertEqual(self.controller.get_click_stats('clicktest'), 0)
        self.controller.redirect_to_long_url('clicktest')
        self.assertEqual(self.controller.get_click_stats('clicktest'), 1)

    def test_delete_expired_urls(self):
        self.controller.create_short_url('https://example.com', custom_alias='expired', expiration_date=datetime.now() - timedelta(days=1))
        self.controller.create_short_url('https://example.com', custom_alias='not_expired', expiration_date=datetime.now() + timedelta(days=1))
        self.controller.delete_expired_urls()
        self.assertIsNone(self.controller.redirect_to_long_url('expired'))
        self.assertEqual(self.controller.redirect_to_long_url('not_expired'), 'https://example.com')


if __name__ == '__main__':
    unittest.main()
