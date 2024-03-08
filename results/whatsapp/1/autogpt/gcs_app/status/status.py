from datetime import datetime, timedelta
from typing import List


class Status:
    def __init__(self, user_id: int, content: str):
        self.user_id = user_id
        self.content = content
        self.timestamp = datetime.now()

    def is_expired(self) -> bool:
        return datetime.now() - self.timestamp > timedelta(hours=24)


class StatusList:
    def __init__(self):
        self.statuses = []

    def add_status(self, status: Status):
        self.statuses.append(status)

    def remove_expired_statuses(self):
        self.statuses = [status for status in self.statuses if not status.is_expired()]

    def get_statuses(self) -> List[Status]:
        return self.statuses