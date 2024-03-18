# URL Shortener

This is a simple URL shortener built with Flask.

## Setup

1. Install Python 3.
2. Install the required packages with `pip install -r requirements.txt`.
3. Run the application with `python3 app.py`.

## Usage

- To shorten a URL, send a POST request to `/shorten` with the following JSON body:

```json
{
	"url": "<original_url>",
	"custom_short_url": "<custom_short_url>",
	"username": "<username>",
	"expiration_date": "<expiration_date>"
}
```

- To access a short URL, simply navigate to `/<short_url>`.

- To get the analytics for a short URL, send a GET request to `/analytics/<short_url>`.

## Running Tests

Run the tests with `pytest`.
