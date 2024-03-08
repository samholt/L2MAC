import pytest
import random
import string
from my_oms import register_user, authenticate_user

def random_string(length=10):
    """Generates a random string of specified length."""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def test_user_registration():
    username = random_string()
    email = f"{random_string()}@example.com"
    password = random_string()
    
    assert register_user(username, email, password) == True

def test_user_authentication():
    username = random_string()
    email = f"{random_string()}@example.com"
    password = random_string()

    register_user(username, email, password)
    assert authenticate_user(email, password) == True

def test_profile_editing():
    user_id = random.randint(1, 1000)
    new_bio = random_string(50)
    new_website = f"https://{random_string()}.com"
    new_location = random_string(15)

    assert edit_profile(user_id, new_bio, new_website, new_location) == True

def test_create_post():
    user_id = random.randint(1, 1000)
    post_content = random_string(280)
    
    assert create_post(user_id, post_content) == True

def test_delete_post():
    user_id = random.randint(1, 1000)
    post_id = create_post(user_id, random_string(280))

    assert delete_post(user_id, post_id) == True

def test_post_interaction():
    user_id = random.randint(1, 1000)
    post_id = create_post(random.randint(1, 1000), random_string(280))

    assert like_post(user_id, post_id) == True
    assert retweet_post(user_id, post_id) == True
    assert reply_to_post(user_id, post_id, random_string(280)) == True

def test_post_search():
    keyword = random_string()
    assert search_posts(keyword) is not None

def test_user_search():
    username = random_string()
    assert search_users(username) is not None

def test_follow_unfollow():
    user_id = random.randint(1, 1000)
    target_user_id = random.randint(1, 1000)

    assert follow_user(user_id, target_user_id) == True
    assert unfollow_user(user_id, target_user_id) == True

def test_direct_messaging():
    sender_id = random.randint(1, 1000)
    receiver_id = random.randint(1, 1000)
    message = random_string(100)

    assert send_message(sender_id, receiver_id, message) == True

def test_notifications():
    user_id = random.randint(1, 1000)
    assert get_notifications(user_id) is not None

def test_trending_topics():
    assert get_trending_topics() is not None

def test_user_recommendations():
    user_id = random.randint(1, 1000)
    assert get_user_recommendations(user_id) is not None
