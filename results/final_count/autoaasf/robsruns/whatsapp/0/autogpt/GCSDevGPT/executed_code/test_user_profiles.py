def test_user_profiles():
    user = User('test', 'password')
    profile = UserProfile(user)
    profile.update_profile_info('email', 'test@example.com')
    assert profile.profile_info['email'] == 'test@example.com'