# Application

This is a simple Flask application.

## Installation

1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.

## Running the Application

1. Run the application using `python3 app.py`.
2. Open your web browser and navigate to `http://localhost:5000`.

## Running the Tests

1. Run the tests using `pytest`.

## Usage

The application provides a simple API. You can make GET and POST requests to `/api/data`.

- GET: Returns all the data.
- POST: Adds new data. The body of the request should be a JSON object.

## Deployment

The application is ready for deployment. You can use any WSGI server, like Gunicorn or uWSGI, to serve the application.
