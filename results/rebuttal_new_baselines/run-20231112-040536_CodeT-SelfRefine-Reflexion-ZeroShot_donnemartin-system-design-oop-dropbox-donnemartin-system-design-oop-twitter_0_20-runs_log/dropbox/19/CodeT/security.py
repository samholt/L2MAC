from dataclasses import dataclass

@dataclass
class ActivityLog:
	user_email: str
	action: str
	timestamp: str

logs = {}

def get_activity_log(data):
	return logs.get(data['user_email'])
