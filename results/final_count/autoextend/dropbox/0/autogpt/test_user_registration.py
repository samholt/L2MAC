from user_registration import register_user


def test_register_user():
    name = 'Test User'
    email = 'test@example.com'
    password = 'test_password'
    register_user(name, email, password)
    print('User registered successfully.')


if __name__ == '__main__':
    test_register_user()