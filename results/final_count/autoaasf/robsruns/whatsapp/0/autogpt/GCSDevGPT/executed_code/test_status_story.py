def test_status_story():
    user1 = User('user1', 'password1')
    status = Status(user1, 'Hello, world!')
    assert status.user == user1
    assert status.text == 'Hello, world!'