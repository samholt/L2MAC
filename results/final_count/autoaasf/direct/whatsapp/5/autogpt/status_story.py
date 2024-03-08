import time


class StatusStory:

    def __init__(self):
        self.status_stories = []

    def add_status_story(self, user_id, content, duration):
        status_story = {
            'user_id': user_id,
            'content': content,
            'timestamp': time.time(),
            'duration': duration
        }
        self.status_stories.append(status_story)

    def get_status_stories(self, user_id, contacts):
        current_time = time.time()
        return [story for story in self.status_stories if story['user_id'] in contacts and current_time - story['timestamp'] <= story['duration']]


if __name__ == '__main__':
    status_story = StatusStory()
    status_story.add_status_story(1, 'Enjoying a beautiful sunset!', 86400)
    status_story.get_status_stories(2, [1])