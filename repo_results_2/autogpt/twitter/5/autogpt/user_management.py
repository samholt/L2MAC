# User Management Code

# User Registration
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.private = False

users = []

def register(username, password):
    new_user = User(username, password)
    users.append(new_user)
    return 'User registered successfully'

# User Authentication
def authenticate(username, password):
    for user in users:
        if user.username == username and user.password == password:
            return 'User authenticated successfully'
    return 'Authentication failed'

# Profile Management
def update_profile(username, password, new_username=None, new_password=None):
    for user in users:
        if user.username == username and user.password == password:
            if new_username:
                user.username = new_username
            if new_password:
                user.password = new_password
            return 'Profile updated successfully'
    return 'Update failed'

# Privacy Settings
def update_privacy(username, password, private):
    for user in users:
        if user.username == username and user.password == password:
            user.private = private
            return 'Privacy settings updated successfully'
    return 'Update failed'