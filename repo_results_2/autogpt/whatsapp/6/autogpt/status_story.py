import time

class StatusStory:
    def __init__(self, user):
        self.user = user
        self.statuses = []

    def post_status(self, image, visibility):
        status = {'image': image, 'posted_at': time.time(), 'visibility': visibility}
        self.statuses.append(status)

    def get_visible_statuses(self):
        current_time = time.time()
        visible_statuses = [status for status in self.statuses if current_time - status['posted_at'] <= 24*60*60]
        return visible_statuses