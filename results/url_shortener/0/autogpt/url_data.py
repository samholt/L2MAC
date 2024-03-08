from datetime import datetime


class URLData:
    def __init__(self, long_url: str, short_url: str, custom_alias: str = None, click_count: int = 0, expiration_date: datetime = None):
        self.long_url = long_url
        self.short_url = short_url
        self.custom_alias = custom_alias
        self.click_count = click_count
        self.expiration_date = expiration_date

    def increment_click_count(self):
        self.click_count += 1
