import datetime


class ActivityLog:
    def __init__(self, user):
        self.user = user
        self.log = []

    def log_action(self, action):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.log.append({'timestamp': timestamp, 'action': action})


if __name__ == '__main__':
    # Retrieve user data securely
    user = None  # Replace with retrieved user data
    activity_log = ActivityLog(user)
    action = 'User uploaded a file'
    activity_log.log_action(action)
    print('Activity logged.')