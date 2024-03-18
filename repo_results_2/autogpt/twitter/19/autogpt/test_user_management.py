import pytest
from user_management import User

def test_user_management():
    user = User()
    user.register('testuser', 'testpassword', 'testuser@example.com')
    assert user.username == 'testuser'
    assert user.password == 'testpassword'
    assert user.email == 'testuser@example.com'
    assert user.authenticate('testuser', 'testpassword')
    user.update_profile({'bio': 'Test user'})
    assert user.profile == {'bio': 'Test user'}
    user.update_privacy_settings({'show_email': False})
    assert user.privacy_settings == {'show_email': False}