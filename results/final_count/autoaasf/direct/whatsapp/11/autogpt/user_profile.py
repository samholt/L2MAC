class UserProfile:
    def __init__(self, user, first_name, last_name, email, bio):
        self.user = user
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.bio = bio

    def update_profile(self, first_name=None, last_name=None, email=None, bio=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if email:
            self.email = email
        if bio:
            self.bio = bio