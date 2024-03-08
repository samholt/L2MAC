import pytest
from random import randint, choices
import string
from datetime import datetime, timedelta

# Helper Functions
def random_url():
    return f"https://example{randint(1000, 9999)}.com"

def random_username():
    return 'user' + ''.join(choices(string.ascii_lowercase + string.digits, k=5))

def random_slug():
    return ''.join(choices(string.ascii_lowercase + string.digits, k=8))

# Test Functions
class TestURLShorteningService:

    def test_input_url_shortening(self):
        url = random_url()
        shortened_url = shorten_url(url)
        assert isinstance(shortened_url, str)
        assert len(shortened_url) < len(url)

    def test_url_validation(self):
        valid_url = random_url()
        invalid_url = "htp:/invalid" + ''.join(choices(string.ascii_lowercase + string.digits, k=10))
        assert validate_url(valid_url) is True
        assert validate_url(invalid_url) is False

    def test_unique_shortened_url(self):
        url = random_url()
        shortened_url1 = shorten_url(url)
        shortened_url2 = shorten_url(url)
        assert shortened_url1 != shortened_url2

    def test_custom_short_link(self):
        url = random_url()
        custom_slug = random_slug()
        custom_short_url = shorten_url(url, custom_slug)
        assert custom_slug in custom_short_url

    def test_redirection(self):
        original_url = random_url()
        shortened_url = shorten_url(original_url)
        redirected_url = redirect(shortened_url)
        assert redirected_url == original_url

    def test_analytics_retrieval(self):
        shortened_url = shorten_url(random_url())
        analytics = get_analytics(shortened_url)
        assert 'clicks' in analytics
        assert 'click_dates' in analytics
        assert 'click_geolocations' in analytics

    def test_user_account_functions(self):
        username = random_username()
        user = create_user(username, "password")
        assert user is not None
        urls = user.get_shortened_urls()
        assert isinstance(urls, list)
        user.edit_url("old_short_url", "new_short_url")
        assert "new_short_url" in user.get_shortened_urls()
        user.delete_url("new_short_url")
        assert "new_short_url" not in user.get_shortened_urls()
        analytics = user.get_analytics("short_url")
        assert analytics is not None

    def test_admin_functions(self):
        admin = create_admin("admin_username", "admin_password")
        all_urls = admin.get_all_urls()
        assert isinstance(all_urls, list)
        admin.delete_url("some_short_url")
        assert "some_short_url" not in admin.get_all_urls()
        admin.delete_user("username")
        assert admin.get_user("username") is None
        system_stats = admin.get_system_stats()
        assert system_stats is not None

    def test_url_expiration(self):
        url = random_url()
        expiration_time = datetime.now() + timedelta(minutes=randint(1, 60))
        shortened_url = shorten_url(url, expiration_time=expiration_time)
        assert check_expiration(shortened_url) is False
        # Additional code to simulate waiting until after expiration may be required
