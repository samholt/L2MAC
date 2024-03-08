class Notification:
    def __init__(self, notification_id, user, message, status):
        self.notification_id = notification_id
        self.user = user
        self.message = message
        self.status = status

    def send_notification(self):
        # logic to send notification
        pass

    def update_notification(self, status):
        self.status = status
