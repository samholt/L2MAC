import hashlib


class CloudSafe:
    def __init__(self):
        self.users = {}
        self.files = {}
        self.file_versions = {}
        self.shared_files = {}
        self.activity_log = {}

    def register_user(self, username, password, email):
        if username in self.users:
            return 'Username already exists'
        if any(user['email'] == email for user in self.users.values()):
            return 'Email already in use'
        self.users[username] = {'password': hashlib.sha256(password.encode()).hexdigest(), 'email': email, 'storage': 0}
        return 'Registration successful'

    def login_user(self, username, password):
        if username not in self.users or self.users[username]['password'] != hashlib.sha256(password.encode()).hexdigest():
            return 'Invalid username or password'
        return 'Login successful'

    def manage_profile(self, username, new_password=None, new_email=None):
        if username not in self.users:
            return 'Invalid username'
        if new_password:
            self.users[username]['password'] = hashlib.sha256(new_password.encode()).hexdigest()
        if new_email:
            if any(user['email'] == new_email for user in self.users.values()):
                return 'Email already in use'
            self.users[username]['email'] = new_email
        return 'Profile updated successfully'

    def track_storage(self, username):
        if username not in self.users:
            return 'Invalid username'
        return self.users[username]['storage']

    def upload_file(self, username, file):
        if username not in self.users:
            return 'Invalid username'
        self.users[username]['storage'] += len(file)
        self.files[username] = hashlib.sha256(file.encode()).hexdigest()
        if username not in self.file_versions:
            self.file_versions[username] = []
        self.file_versions[username].append(hashlib.sha256(file.encode()).hexdigest())
        return 'File uploaded successfully'

    def download_file(self, username):
        if username not in self.users or username not in self.files:
            return 'Invalid username or no file found'
        return self.files[username]

    def organize_files(self, username, action, file=None):
        if username not in self.users:
            return 'Invalid username'
        if action == 'rename' and file:
            self.files[username] = hashlib.sha256(file.encode()).hexdigest()
        elif action == 'delete':
            del self.files[username]
            self.users[username]['storage'] = 0
        return 'File organized successfully'

    def version_files(self, username):
        if username not in self.users or username not in self.file_versions:
            return 'Invalid username or no file versions found'
        return self.file_versions[username]

    def share_file(self, username, recipient, password=None, expiry_date=None):
        if username not in self.users or recipient not in self.users or username not in self.files:
            return 'Invalid username or recipient or no file found'
        self.shared_files[recipient] = {'file': self.files[username], 'password': password, 'expiry_date': expiry_date}
        return 'File shared successfully'

    def log_activity(self, username, action):
        if username not in self.users:
            return 'Invalid username'
        if username not in self.activity_log:
            self.activity_log[username] = []
        self.activity_log[username].append(action)
        return 'Activity logged successfully'