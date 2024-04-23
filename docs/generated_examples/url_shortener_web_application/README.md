# URL Shortening Service

This project is a simple URL shortening service built with Flask. It allows users to submit long URLs and receive a shortened version for ease of sharing. Additionally, it supports user registration and login, URL analytics, and admin functionalities.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- pip

### Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies:

```
pip install -r requirements.txt
```

Or run the provided shell script:

```
./run.sh
```

### Running the Application

To run the Flask application:

```
python app.py
```

Or use the entry point created by the setup.py:

```
url-shortener
```

### Using the Service

- To shorten a URL, navigate to the home page, enter the URL in the provided form, and click `Shorten`.
- To register or login, use the links provided on the home page. Once logged in, you can access additional features such as viewing and managing your shortened URLs and viewing analytics.
- Admin users can view all shortened URLs, delete URLs or user accounts, and monitor system performance from the admin dashboard.

### Running Tests

To run the tests, execute the following command:

```
pytest
```

## Project Structure

- `app.py`: The main Flask application file.
- `requirements.txt`: Lists all the project dependencies.
- `templates/`: Contains HTML templates for the web interface.
- `static/`: Contains CSS and JavaScript files for the web interface.
- `tests/`: Contains pytest tests for the application.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

