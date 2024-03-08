from dataclasses import dataclass

@dataclass
class Activity:
	user_email: str
	action: str

activities = []


def get_activity_log():
	return [activity.__dict__ for activity in activities], 200
