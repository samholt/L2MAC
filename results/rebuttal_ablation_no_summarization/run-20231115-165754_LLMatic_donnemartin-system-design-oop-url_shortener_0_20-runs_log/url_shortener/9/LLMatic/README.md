# URL Shortener

This is a simple URL shortener application built with Flask.

## Setup

1. Install the required packages with `pip install -r requirements.txt`
2. Run the application with `python3 app.py`

## Usage

- To create a short URL, send a POST request to `/create_url` with the original URL and optional custom alias and expiration date.
- To view a short URL, send a GET request to `/<short_url>`.
- To view all short URLs, send a GET request to `/admin/urls`.
- To delete a short URL, send a DELETE request to `/admin/delete_url/<short_url>`.
- To create a user account, send a POST request to `/create_account` with the username.
- To view URLs of a user account, send a GET request to `/view_urls/<username>`.
- To edit a URL of a user account, send a PUT request to `/edit_url/<username>/<short_url>` with the new URL.
- To delete a URL of a user account, send a DELETE request to `/delete_url/<username>/<short_url>`.
- To delete a user account, send a DELETE request to `/delete_account/<username>`.
- To view analytics data, send a GET request to `/admin/analytics`.

## Testing

Run the tests with `pytest`.
