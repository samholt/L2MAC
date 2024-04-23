from datetime import datetime, timedelta

import pytest
from app import app as flask_app
from app import generate_short_url, urls_db, users_db


@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client


# Test admin dashboard functionality
def test_admin_access(client):
    # Attempt to access admin routes without being logged in
    response = client.get("/admin/urls")
    assert response.status_code == 401

    # Login as a regular user
    client.post("/register", data={"username": "regular", "password": "user"})
    client.post("/login", data={"username": "regular", "password": "user"})
    response = client.get("/admin/urls")
    assert response.status_code == 401

    # Login as admin
    client.post("/login", data={"username": "admin", "password": "admin"})
    response = client.get("/admin/urls")
    assert response.status_code == 200

    # Test deleting a URL as admin
    short_url = generate_short_url()
    urls_db[short_url] = {"url": "http://example.com", "expiration": datetime.now() + timedelta(days=1)}
    response = client.delete(f"/admin/delete/url/{short_url}")
    assert response.status_code == 200
    assert short_url not in urls_db

    # Test deleting a user as admin
    response = client.delete("/admin/delete/user/regular")
    assert response.status_code == 200
    assert "regular" not in users_db


# Test URL expiration functionality
def test_url_expiration(client):
    # Create a URL that expires in the past
    expired_short_url = generate_short_url()
    urls_db[expired_short_url] = {"url": "http://expired.com", "expiration": datetime.now() - timedelta(days=1)}
    response = client.get(f"/{expired_short_url}")
    assert response.status_code == 410
    assert "URL has expired" in response.get_data(as_text=True)

    # Create a URL that does not expire
    non_expired_short_url = generate_short_url()
    urls_db[non_expired_short_url] = {"url": "http://nonexpired.com", "expiration": datetime.now() + timedelta(days=1)}
    response = client.get(f"/{non_expired_short_url}")
    assert response.status_code == 302  # Redirect status code
