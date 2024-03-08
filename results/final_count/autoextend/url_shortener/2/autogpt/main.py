from url_shortener import URLShortener, User, Admin
from analytics import Analytics


if __name__ == '__main__':
    analytics = Analytics()
    url_shortener = URLShortener()
    user = User(analytics)
    admin = Admin(analytics)

    # Example usage:
    # url_shortener.shorten_url('https://example.com')
    # user.view_analytics('short_url')
    # admin.delete_url('short_url')