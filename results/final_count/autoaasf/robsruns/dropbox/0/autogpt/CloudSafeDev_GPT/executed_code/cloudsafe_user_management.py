class CloudSafe:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password, email):
        if username in self.users:
            return 'Username already exists'
        if any(user['email'] == email for user in self.users.values()):
            return 'Email already in use'
        self.users[username] = {'password': password, 'email': email, 'storage': 0}
        return 'Registration successful'

    def login_user(self, username, password):
        if username not in self.users or self.users[username]['password'] != password:
            return 'Invalid username or password'
        return 'Login successful'

    def manage_profile(self, username, new_password=None, new_email=None):
        if username not in self.users:
            return 'Invalid username'
        if new_password:
            self.users[username]['password'] = new_password
        if new_email:
            if any(user['email'] == new_email for user in self.users.values()):
                return 'Email already in use'
            self.users[username]['email'] = new_email
        return 'Profile updated successfully'

    def track_storage(self, username):
        if username not in self.users:
            return 'Invalid username'
        return self.users[username]['storage']