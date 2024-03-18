import pytest
from user_management import User
from content_management import Post

def test_content_management():
    user = User()
    user.register('testuser', 'testpassword', 'testuser@example.com')
    post = Post()
    post.create_post(user, 'Test post')
    assert post.user == user
    assert post.content == 'Test post'
    post.interact_with_post(user, 'like')
    assert post.interactions[user] == 'like'
    assert post.filter_content('Test')
    assert post.search_content('post')