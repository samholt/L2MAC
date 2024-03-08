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

    def create_status_story(self, user, content, duration):
        status_story = StatusStory(user, content, duration)
        if user.username not in self.status_stories:
            self.status_stories[user.username] = []
        self.status_stories[user.username].append(status_story)

    def get_status_stories(self, username):
        if username not in self.status_stories:
            return []
        return [story for story in self.status_stories[username] if not story.is_expired()]