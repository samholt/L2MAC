import hashlib
import uuid


class UserAuth:

    def __init__(self):
        self.users = {}

    @staticmethod
    def hash_password(password, salt):
        return hashlib.sha256((password + salt).encode('utf-8')).hexdigest()

    @staticmethod
    def generate_salt():
        return uuid.uuid4().hex

    def register_user(self, username, password, email):
        salt = self.generate_salt()
        hashed_password = self.hash_password(password, salt)
        user_id = len(self.users) + 1
        self.users[user_id] = {'username': username, 'password': hashed_password, 'email': email, 'salt': salt}
        return user_id

    def authenticate_user(self, username, password):
        for user_id, user_data in self.users.items():
            if user_data['username'] == username:
                hashed_password = self.hash_password(password, user_data['salt'])
                if user_data['password'] == hashed_password:
                    return user_id
        return None


if __name__ == '__main__':
    user_auth = UserAuth()
    user_id = user_auth.register_user('test_user', 'password123', 'test@example.com')
    authenticated_user_id = user_auth.authenticate_user('test_user', 'password123')
    print(authenticated_user_id)