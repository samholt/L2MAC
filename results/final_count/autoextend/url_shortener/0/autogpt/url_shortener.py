import random
import string


class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, original_url: str) -> str:
        shortened_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        self.url_mapping[shortened_url] = original_url
        return shortened_url

    def get_original_url(self, shortened_url: str) -> str:
        return self.url_mapping.get(shortened_url, None)