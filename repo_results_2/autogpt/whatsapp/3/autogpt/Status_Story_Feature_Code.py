import time

class Status:
    def __init__(self, user, image, visibility, duration=24*60*60):
        self.user = user
        self.image = image
        self.visibility = visibility
        self.post_time = time.time()
        self.duration = duration

    def is_visible(self):
        return time.time() - self.post_time <= self.duration

class StatusManagement:
    def __init__(self):
        self.statuses = []

    def post_status(self, user, image, visibility):
        self.statuses.append(Status(user, image, visibility))

    def view_status(self, viewer, status):
        if status.is_visible() and (status.visibility == 'public' or viewer in status.user.contacts):
            return status.image
        return None