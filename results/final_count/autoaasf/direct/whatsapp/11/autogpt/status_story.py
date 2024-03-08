import datetime

class StatusStory:
    def __init__(self, user, content, duration):
        self.user = user
        self.content = content
        self.duration = duration
        self.timestamp = datetime.datetime.now()

    def is_active(self):
        return (datetime.datetime.now() - self.timestamp).total_seconds() <= self.duration

class StatusStoryManager:
    def __init__(self, user):
        self.user = user
        self.status_stories = []

    def add_status_story(self, content, duration):
        status_story = StatusStory(self.user, content, duration)
        self.status_stories.append(status_story)

    def get_active_status_stories(self):
        return [story for story in self.status_stories if story.is_active()]