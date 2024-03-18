import time

class Status:
    def __init__(self, user, image, visibility):
        self.user = user
        self.image = image
        self.visibility = visibility
        self.post_time = time.time()

    def is_visible(self):
        # Status is visible for 24 hours
        return time.time() - self.post_time <= 24 * 60 * 60

    def can_see(self, user):
        # Implementation of visibility control not included
        pass