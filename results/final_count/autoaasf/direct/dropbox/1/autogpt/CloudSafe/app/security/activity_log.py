class ActivityLogEntry:
    def __init__(self, user, action, timestamp):
        self.user = user
        self.action = action
        self.timestamp = timestamp


def log_activity(user, action):
    timestamp = time.time()
    entry = ActivityLogEntry(user, action, timestamp)
    # TODO: Save the activity log entry to the database
    return entry