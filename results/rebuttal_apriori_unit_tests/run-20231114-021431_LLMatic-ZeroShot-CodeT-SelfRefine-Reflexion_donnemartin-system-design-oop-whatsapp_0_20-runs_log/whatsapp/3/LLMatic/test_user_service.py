import pytest
import random
import string

from user_service import UserService

user_service = UserService()


def test_set_profile_picture_and_status():
    user_id = random.randint(1, 100)
    picture_path = f"/path/to/picture{random.randint(1, 5)}.jpg"
    status_message = f"Status {random.randint(1, 100)}"
    assert user_service.set_profile(user_id, picture_path, status_message) == True


def test_privacy_settings():
    user_id = random.randint(1, 100)
    privacy_settings = random.choice(['Everyone', 'Contacts', 'Nobody'])
    assert user_service.set_privacy(user_id, privacy_settings) == True
