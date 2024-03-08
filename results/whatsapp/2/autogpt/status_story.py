import time


class StatusStory:
    def __init__(self, user_profile, content, duration):
        self.user_profile = user_profile
        self.content = content
        self.duration = duration
        self.timestamp = time.time()

    def is_expired(self):
        return time.time() - self.timestamp > self.duration


def create_status_story(user_profile, content, duration):
    return StatusStory(user_profile, content, duration)