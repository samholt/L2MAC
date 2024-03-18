class UserProfile:
    def __init__(self, user):
        self.user = user
        self.bio = ''
        self.location = ''
        self.website = ''

    def update_bio(self, bio):
        self.bio = bio

    def update_location(self, location):
        self.location = location

    def update_website(self, website):
        self.website = website