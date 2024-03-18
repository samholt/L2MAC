class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserManager:
    def register(self, username, password):
        return User(username, password)
    def authenticate(self, username, password):
        # This is a placeholder. In a real system, we would check the username and password against a database.
        return username == 'admin' and password == 'password'