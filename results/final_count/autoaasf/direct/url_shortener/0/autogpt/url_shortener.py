import random
import string


class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def generate_short_url(self, original_url: str) -> str:
        unique_key = self.generate_unique_key()
        short_url = f'https://short.url/{unique_key}'
        self.store_url_mapping(original_url, short_url)
        return short_url

    def get_original_url(self, short_url: str) -> str:
        return self.url_mapping.get(short_url, '')

    def store_url_mapping(self, original_url: str, short_url: str):
        self.url_mapping[short_url] = original_url

    def generate_unique_key(self) -> str:
        key_length = 6
        return ''.join(random.choices(string.ascii_letters + string.digits, k=key_length))