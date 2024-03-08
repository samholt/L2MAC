# Global Chat Service (GCS) Application

This application provides a global chat service with the following features:

- User registration and authentication
- User profiles
- Contact management
- Messaging
- Group chats
- Status/story feature
- Web application
- Connectivity and offline mode

## Classes and Modules

- `user_auth.py`: Contains the `UserManager` and `User` classes for user registration and authentication.
- `user_profiles.py`: Contains the `UserProfileManager` class for managing user profiles.
- `contact_management.py`: Contains the `ContactManager` class for managing user contacts.
- `messaging.py`: Contains the `MessageManager` and `Message` classes for messaging functionality.
- `group_chats.py`: Contains the `GroupChatManager` and `GroupChat` classes for group chat functionality.
- `status_story.py`: Contains the `StatusStoryManager` and `StatusStory` classes for the status/story feature.
- `web_application.py`: Contains the Flask web application for the user interface.
- `connectivity_offline.py`: Contains the `DataStore` class for saving and loading application state.
- `tests.py`: Contains the `TestGCS` class for testing the application.

## Running the Application

1. Install the required dependencies: `pip install -r requirements.txt`
2. Run the Flask web application: `python web_application.py`
3. Access the application in your web browser at `http://localhost:5000`.

## Running the Tests

To run the tests, execute the following command: `python -m unittest tests.py`