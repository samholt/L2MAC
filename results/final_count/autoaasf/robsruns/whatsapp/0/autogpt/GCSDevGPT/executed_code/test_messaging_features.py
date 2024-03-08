def test_messaging_features():
    user1 = User('user1', 'password1')
    user2 = User('user2', 'password2')
    message = Message(user1, user2, 'Hello, world!')
    assert message.sender == user1
    assert message.recipient == user2
    assert message.text == 'Hello, world!'