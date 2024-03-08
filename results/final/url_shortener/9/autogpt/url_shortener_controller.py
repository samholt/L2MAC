import random
import string
from datetime import datetime
from url_data import URLData
from url_shortener_view import URLShortenerView


class URLShortenerController:
    def __init__(self):
        self.url_data_store = {}

    def create_short_url(self, long_url: str, custom_alias: str = None, expiration_date: datetime = None):
        if custom_alias:
            short_url = custom_alias
        else:
            short_url = self._generate_random_short_url()

        if short_url in self.url_data_store:
            URLShortenerView.display_error('Short URL already exists.')
            return

        url_data = URLData(long_url, short_url, custom_alias, expiration_date=expiration_date)
        self.url_data_store[short_url] = url_data
        URLShortenerView.display_short_url(short_url)
        return short_url

    def _generate_random_short_url(self, length: int = 6):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def redirect_to_long_url(self, short_url: str):
        url_data = self.url_data_store.get(short_url)
        if url_data:
            url_data.increment_click_count()
            return url_data.long_url
        else:
            URLShortenerView.display_error('Short URL not found.')
            return None

    def get_click_stats(self, short_url: str):
        url_data = self.url_data_store.get(short_url)
        if url_data:
            return url_data.click_count
        else:
            URLShortenerView.display_error('Short URL not found.')
            return None

    def delete_expired_urls(self):
        current_time = datetime.now()
        expired_urls = [short_url for short_url, url_data in self.url_data_store.items() if url_data.expiration_date and url_data.expiration_date <= current_time]
        for short_url in expired_urls:
            del self.url_data_store[short_url]
