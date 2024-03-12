# URL Shortener

This project is a URL shortener service. It allows users to input a long URL and get a shortened version that redirects to the original URL. It also provides analytics about the usage of the shortened URLs and an admin dashboard for managing the system.

## Setup

1. Install Python 3.7 or higher.
2. Install the required packages using pip:

```
pip install -r requirements.txt
```

3. Run the application:

```
python3 app.py
```

## Usage

### URL Shortening

Use the `url_shortener.shorten_url` function to shorten a URL. It takes a long URL as input and returns a shortened URL.

### Analytics

The `analytics.get_url_data` function provides analytics data for a shortened URL. It returns the number of times the URL has been accessed and the last access time.

### User Accounts

Users can register and login using the `user_accounts.register` and `user_accounts.login` functions. Registered users can manage their own shortened URLs.

### Admin Dashboard

The admin dashboard provides an overview of the system's usage. It can be accessed using the `admin_dashboard.get_dashboard_data` function.

## Code Documentation

The code is well-documented with comments explaining the logic. For complex parts of the code, refer to the comments in the respective files.

## Testing

Tests for the application are written using pytest. To run the tests, use the following command:

```
pytest
```

The tests cover all the features and edge cases of the application.
