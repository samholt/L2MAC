from dataclasses import dataclass

@dataclass
class Activity:
	user_email: str
	action: str

activities = {}


def encrypt_file(data):
	return {'status': 'success', 'message': 'File encrypted successfully'}

def activity_log(data):
	activity = Activity(**data)
	activities[activity.user_email] = activity
	return {'status': 'success', 'message': 'Activity logged successfully'}
