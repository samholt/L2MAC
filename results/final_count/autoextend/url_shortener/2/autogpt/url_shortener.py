from analytics import Analytics

class URLShortener:
    def __init__(self):
        pass

    def validate_url(self, url):
        pass

    def generate_shortened_url(self, url):
        pass

    def shorten_url(self, url, custom_alias=None):
        pass

    def redirect_to_original_url(self, short_url):
        pass

class User:
    def __init__(self, analytics):
        self.analytics = analytics

    def create_account(self, username, password):
        pass

    def view_shortened_urls(self):
        pass

    def edit_url(self, short_url, new_url):
        pass

    def delete_url(self, short_url):
        pass

    def view_analytics(self, short_url):
        return self.analytics.view_statistics(short_url)

class Admin(User):
    def __init__(self, analytics):
        super().__init__(analytics)

    def view_shortened_urls(self):
        pass

    def delete_url(self, short_url):
        pass

    def delete_user_account(self, username):
        pass

    def monitor_performance(self):
        pass

    def set_url_expiration(self, short_url, expiration_datetime):
        pass