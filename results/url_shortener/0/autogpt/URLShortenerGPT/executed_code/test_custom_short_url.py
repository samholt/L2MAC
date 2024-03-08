from url_shortener_controller import URLShortenerController

controller = URLShortenerController()
controller.create_short_url('https://example.com', custom_alias='custom')
print(controller.redirect_to_long_url('custom'))