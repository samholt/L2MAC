# URL Shortener

This is a simple URL shortener application built with Flask.

## Setup

1. Install the required packages with `pip install -r requirements.txt`
2. Run the application with `python3 app.py`

## Usage

- To shorten a URL, send a POST request to `/shorten` with the URL as form data.
- To view the original URL of a shortened URL, send a GET request to `/<short_url>`.
- To create a user, send a POST request to `/user/create` with the username and password as form data.
- To view a user's URLs, send a GET request to `/user/<username>/urls`.
- To view a user's analytics, send a GET request to `/user/<username>/analytics`.
- To set a URL's expiration date, send a POST request to `/user/<username>/set-expiration` with the short URL and expiration date as form data.
- To create an admin, send a POST request to `/admin/create` with the username and password as form data.
- To view all URLs as an admin, send a GET request to `/admin/<username>/urls`.
- To delete a user as an admin, send a POST request to `/admin/<username>/delete-user` with the username of the user to delete as form data.

## Running Tests

Run the tests with `pytest`.

## Code Structure

- `app.py`: This is the main application file. It defines the routes and handles the requests.
- `shortener.py`: This file contains the `Shortener` class, which handles the URL shortening logic.
- `user.py`: This file contains the `User` class, which represents a user of the application.
- `admin.py`: This file contains the `Admin` class, which represents an admin of the application.
- `test_*.py`: These files contain the tests for the application.
