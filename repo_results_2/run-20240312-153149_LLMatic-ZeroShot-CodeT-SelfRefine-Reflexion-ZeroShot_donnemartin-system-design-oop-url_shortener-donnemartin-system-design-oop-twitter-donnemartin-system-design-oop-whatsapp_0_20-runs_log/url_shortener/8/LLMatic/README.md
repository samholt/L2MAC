# URL Shortener

This is a simple URL shortener application built with Flask.

## Running the Application

1. Install the required packages with `pip install -r requirements.txt`
2. Run the application with `python3 app.py`

The application will start on `http://localhost:5000`.

## Running the Tests

Run the tests with `pytest`.

## Using the Application

The application provides the following endpoints:

- `POST /shorten_url`: Shorten a URL. The original URL should be provided in the request body as `original_url`.
- `GET /<short_url>`: Redirect to the original URL associated with the short URL.
- `POST /user/create`: Create a new user. The username and password should be provided in the request body as `username` and `password`.
- `POST /user/add_url`: Add a new URL for the user. The username and original URL should be provided in the request body as `username` and `long_url`.
- `GET /user/view_urls`: View all URLs of the user. The username should be provided as a query parameter.
- `PUT /user/edit_url`: Edit a URL of the user. The username, short URL, and new original URL should be provided in the request body as `username`, `short_url`, and `new_long_url`.
- `DELETE /user/delete_url`: Delete a URL of the user. The username and short URL should be provided in the request body as `username` and `short_url`.
- `GET /user/view_analytics`: View analytics of a URL of the user. The username and short URL should be provided as query parameters.
- `GET /admin/view_all_urls`: View all URLs in the system.
- `DELETE /admin/delete_url`: Delete a URL from the system. The short URL should be provided in the request body as `short_url`.
- `DELETE /admin/delete_user`: Delete a user from the system. The username should be provided in the request body as `username`.
- `GET /admin/monitor_system`: Monitor the system.
