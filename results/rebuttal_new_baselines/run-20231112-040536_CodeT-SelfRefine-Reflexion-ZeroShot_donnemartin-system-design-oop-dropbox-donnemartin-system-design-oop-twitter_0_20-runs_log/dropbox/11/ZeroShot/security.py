from dataclasses import dataclass

@dataclass
class Activity:
	user_email: str
	action: str

activities = {}


def encrypt_file(data):
	return {'message': 'File encrypted successfully'}

def activity_log(data):
	activity = Activity(**data)
	activities[activity.user_email] = activity
	return {'message': 'Activity logged successfully'}
