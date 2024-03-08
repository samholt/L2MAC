import hashlib


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = self.hash_password(password)

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()


def login_user(email, password):
    # Retrieve user data securely
    # Compare hashed password with stored hashed password
    # If match, return success message


if __name__ == '__main__':
    email = input('Enter your email: ')
    password = input('Enter your password: ')
    login_user(email, password)
    print('User logged in successfully.')