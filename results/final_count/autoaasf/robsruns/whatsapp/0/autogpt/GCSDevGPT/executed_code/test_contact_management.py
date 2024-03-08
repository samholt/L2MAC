def test_contact_management():
    user1 = User('user1', 'password1')
    user2 = User('user2', 'password2')
    contact_management = ContactManagement(user1)
    contact_management.add_contact(user2)
    assert user2.username in contact_management.contacts
    contact_management.remove_contact(user2)
    assert user2.username not in contact_management.contacts