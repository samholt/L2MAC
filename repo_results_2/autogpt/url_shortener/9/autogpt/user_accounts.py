import hashlib

class UserAccounts:
    def __init__(self):
        self.user_dict = {}

    def register(self, email, password):
        if email in self.user_dict:
            return 'Error: This email is already in use.'
        else:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            self.user_dict[email] = hashed_password
            return 'Success: Your account has been created.'

    def login(self, email, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if self.user_dict.get(email, '') == hashed_password:
            return 'Success: You are now logged in.'
        else:
            return 'Error: Invalid email or password.'