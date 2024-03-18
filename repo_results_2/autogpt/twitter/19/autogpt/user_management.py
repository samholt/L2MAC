import dataclasses

@dataclasses.dataclass
class User:
    username: str
    password: str
    email: str
    profile: dict
    privacy_settings: dict

    def register(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.profile = {}
        self.privacy_settings = {}

    def authenticate(self, username, password):
        return self.username == username and self.password == password

    def update_profile(self, profile):
        self.profile = profile

    def update_privacy_settings(self, privacy_settings):
        self.privacy_settings = privacy_settings