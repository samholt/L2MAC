# URL Shortener

This is a simple URL shortener application built with Flask.

## Setup

1. Install the required Python packages with `pip install -r requirements.txt`.
2. Run the application with `python3 app.py`.

## Usage

- To shorten a URL, send a POST request to `/shorten` with a JSON body containing the `url` key and the URL you want to shorten as the value.
- To view a shortened URL, simply navigate to `/<short_url>`.
- To view analytics for a shortened URL, navigate to `/analytics/<short_url>`.
- To create a user account, send a POST request to `/user/create` with a JSON body containing the `username` and `password` keys.
- To log in a user, send a POST request to `/user/login` with a JSON body containing the `username` and `password` keys.
- To log out a user, send a POST request to `/user/logout` with a JSON body containing the `username` key.
- To view all URLs in the system (admin only), navigate to `/admin/view_urls`.
