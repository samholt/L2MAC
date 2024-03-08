from url_shortener_controller import URLShortenerController


def test_custom_short_url():
    controller = URLShortenerController()
    controller.create_short_url('https://example.com', custom_alias='custom')
    assert controller.redirect_to_long_url('custom') == 'https://example.com'


test_custom_short_url()
