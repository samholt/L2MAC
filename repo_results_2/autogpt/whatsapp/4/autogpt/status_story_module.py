import time

class Status:
    def __init__(self, user, image, visibility):
        self.user = user
        self.image = image
        self.visibility = visibility
        self.timestamp = time.time()

    def is_visible(self):
        return time.time() - self.timestamp < 24 * 60 * 60


class StatusStoryModule:
    def __init__(self):
        self.statuses = []

    def post_status(self, user, image, visibility):
        status = Status(user, image, visibility)
        self.statuses.append(status)
        return status