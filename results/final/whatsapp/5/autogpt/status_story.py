import time


class StatusStory:
    def __init__(self, user, content, duration):
        self.user = user
        self.content = content
        self.duration = duration
        self.timestamp = time.time()

    def is_expired(self):
        return time.time() - self.timestamp > self.duration


class StatusStoryManager:
    def __init__(self):
        self.status_stories = {}

    def add_status_story(self, user, content, duration):
        status_story = StatusStory(user, content, duration)
        self.status_stories[user.username] = status_story

    def get_status_story(self, user):
        status_story = self.status_stories.get(user.username, None)
        if status_story and not status_story.is_expired():
            return status_story
        return None