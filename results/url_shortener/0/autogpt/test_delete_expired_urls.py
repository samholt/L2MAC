from datetime import datetime, timedelta
from url_shortener_controller import URLShortenerController


def test_delete_expired_urls():
    controller = URLShortenerController()
    controller.create_short_url('https://example.com', custom_alias='expired', expiration_date=datetime.now() - timedelta(days=1))
    controller.create_short_url('https://example.com', custom_alias='not_expired', expiration_date=datetime.now() + timedelta(days=1))
    controller.delete_expired_urls()
    assert controller.redirect_to_long_url('expired') is None
    assert controller.redirect_to_long_url('not_expired') == 'https://example.com'


test_delete_expired_urls()
