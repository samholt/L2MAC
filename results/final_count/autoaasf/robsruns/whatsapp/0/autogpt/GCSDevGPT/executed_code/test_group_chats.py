def test_group_chats():
    user1 = User('user1', 'password1')
    user2 = User('user2', 'password2')
    group_chat = GroupChat('Test Group')
    group_chat.add_member(user1)
    group_chat.add_member(user2)
    assert user1 in group_chat.members
    assert user2 in group_chat.members
    message = Message(user1, group_chat, 'Hello, group!')
    group_chat.send_message(message)
    assert message in group_chat.messages
    group_chat.remove_member(user2)
    assert user2 not in group_chat.members