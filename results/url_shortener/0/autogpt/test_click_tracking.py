from url_shortener_controller import URLShortenerController


def test_click_tracking():
    controller = URLShortenerController()
    controller.create_short_url('https://example.com', custom_alias='clicktest')
    assert controller.get_click_stats('clicktest') == 0
    controller.redirect_to_long_url('clicktest')
    assert controller.get_click_stats('clicktest') == 1


test_click_tracking()
