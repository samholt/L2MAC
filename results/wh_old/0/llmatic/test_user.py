from user import User
def test_user():
    user = User(1, 'User 1')
    assert user.user_id == 1
    assert user.name == 'User 1'
    assert user.connection_status == False
