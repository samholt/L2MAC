def test_user_registration_authentication():
    user = User('test', 'password')
    assert user.authenticate('test', 'password') == True
    assert user.authenticate('test', 'wrong_password') == False