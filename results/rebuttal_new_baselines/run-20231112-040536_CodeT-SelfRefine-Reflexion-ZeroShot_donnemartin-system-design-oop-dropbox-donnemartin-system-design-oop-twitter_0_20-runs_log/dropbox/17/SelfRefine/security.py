from dataclasses import dataclass

@dataclass
class Activity:
	user: str
	action: str

activity_log_db = {}


def encryption(data):
	return {'status': 'success', 'message': 'File encrypted successfully'}

def activity_log(data):
	activity = Activity(**data)
	activity_log_db[activity.user] = activity
	return {'status': 'success', 'message': 'Activity logged successfully'}
