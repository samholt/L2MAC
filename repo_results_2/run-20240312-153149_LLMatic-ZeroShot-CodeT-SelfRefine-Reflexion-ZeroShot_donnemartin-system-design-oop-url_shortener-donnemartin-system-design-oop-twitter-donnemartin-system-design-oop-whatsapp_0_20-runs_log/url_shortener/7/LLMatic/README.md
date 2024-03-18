# URL Shortener Application

This application provides a URL shortening service. It also includes user account management, analytics, and an admin dashboard.

## How to Run the Application

1. Install the required packages by running `pip install -r requirements.txt`.
2. Run the application with `python3 app.py`.

## API Usage

### URL Shortener

- `shorten_url(url: str) -> str`: Returns a shortened URL.
- `get_original_url(short_url: str) -> str`: Returns the original URL for a given short URL.

### User Accounts

- `create_user(username: str, password: str) -> bool`: Creates a new user account. Returns True if successful, False otherwise.
- `login(username: str, password: str) -> bool`: Logs in a user. Returns True if successful, False otherwise.

### Analytics

- `get_url_clicks(short_url: str) -> int`: Returns the number of clicks for a given short URL.

### Admin Dashboard

- `get_all_urls() -> List[str]`: Returns a list of all shortened URLs.
- `get_all_users() -> List[str]`: Returns a list of all users.

## Testing

Run the tests with `pytest`.
