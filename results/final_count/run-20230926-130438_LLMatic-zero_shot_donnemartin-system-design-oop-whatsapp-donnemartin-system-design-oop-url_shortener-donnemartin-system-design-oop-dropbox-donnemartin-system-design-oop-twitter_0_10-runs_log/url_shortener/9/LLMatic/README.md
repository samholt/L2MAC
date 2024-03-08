# URL Shortener

This project is a URL shortener service. It provides the following features:

- URL shortening: Users can provide a long URL and receive a shortened URL in return.
- Analytics: Users can view analytics for their shortened URLs, such as the number of clicks.
- User accounts: Users can create an account to manage their URLs.
- Admin dashboard: Admins can view and manage all URLs in the system.

## Setup

1. Install Python 3.8 or higher.
2. Install the required packages with `pip install -r requirements.txt`.
3. Run the application with `python3 app.py`.

## Usage

- To shorten a URL, send a POST request to `/shorten_url` with the long URL in the request body.
- To view analytics for a URL, send a GET request to `/analytics` with the short URL in the request parameters.
- To create a user account, send a POST request to `/create_user` with the username and password in the request body.
- To log in, send a POST request to `/login` with the username and password in the request body.
- To view the admin dashboard, send a GET request to `/admin_dashboard`.

## Testing

Run the tests with `pytest`.

## Code Structure

- `app.py`: The main application file. It sets up the Flask application and routes.
- `url_shortener.py`: Contains the logic for shortening URLs.
- `analytics.py`: Contains the logic for viewing URL analytics.
- `user_accounts.py`: Contains the logic for user account management.
- `admin_dashboard.py`: Contains the logic for the admin dashboard.
- `test_*.py`: Test files for the corresponding modules.
