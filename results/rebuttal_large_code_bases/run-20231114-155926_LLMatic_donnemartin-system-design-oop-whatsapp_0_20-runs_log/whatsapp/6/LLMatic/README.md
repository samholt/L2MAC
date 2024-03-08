# Chat Application

This is a chat application built with Python and Flask. It supports features such as user authentication, profile management, contacts management, group chats, status updates, and web connectivity.

## Setup and Running

1. Clone the repository.
2. Install the dependencies by running `pip install -r requirements.txt`.
3. Run the application by executing `python3 main.py`.

## Dependencies

- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Login
- Flask-WTF
- WTForms
- Python-dotenv

## Testing

Tests are located in the 'tests' directory. Run the tests by executing `pytest`.

## Modules

- `app/__init__.py`: Initializes the Flask application.
- `app/models.py`: Defines the database models.
- `app/auth.py`: Handles user authentication.
- `app/profile.py`: Manages user profiles.
- `app/contacts.py`: Manages user contacts.
- `app/groups.py`: Manages group chats.
- `app/chat.py`: Handles chat functionality.
- `app/status.py`: Manages user status updates.
- `app/web.py`: Handles web connectivity.
- `app/connectivity.py`: Manages connectivity.
- `main.py`: Entry point of the application.

## Tests

- `tests/test_models.py`: Tests for the database models.
- `tests/test_auth.py`: Tests for user authentication.
- `tests/test_profile.py`: Tests for user profiles.
- `tests/test_contacts.py`: Tests for user contacts.
- `tests/test_groups.py`: Tests for group chats.
- `tests/test_chat.py`: Tests for chat functionality.
- `tests/test_status.py`: Tests for user status updates.
- `tests/test_web.py`: Tests for web connectivity.
- `tests/test_connectivity.py`: Tests for connectivity.
