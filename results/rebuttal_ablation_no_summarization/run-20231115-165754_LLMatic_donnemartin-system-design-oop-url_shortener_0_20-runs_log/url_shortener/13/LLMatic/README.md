# URL Shortening Service

This is a simple URL shortening service implemented in Python using Flask.

## Setup

1. Install the required Python packages: `pip install -r requirements.txt`
2. Run the application: `python3 app.py`

## Usage

- To shorten a URL, send a POST request to `/shorten` with the original URL and an optional custom alias and username in the JSON body.
- To redirect a short URL to the original URL, send a GET request to `/<short_url>`.
- To view the analytics of a short URL, send a GET request to `/analytics/<short_url>`.
- To manage a user account, send a POST, PUT, or DELETE request to `/account` with the username and optional new username in the JSON body.
- To view all shortened URLs and users or delete a URL or user account, send a GET or DELETE request to `/admin` with the optional username or short URL in the JSON body.
