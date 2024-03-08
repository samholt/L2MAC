class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __str__(self):
        return f'User({self.username}, {self.email})'

    def change_password(self, new_password):
        self.password = new_password

    def update_email(self, new_email):
        self.email = new_email

    def update_username(self, new_username):
        self.username = new_username