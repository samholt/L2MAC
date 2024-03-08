from dataclasses import dataclass

@dataclass
class Activity:
	user: str
	action: str

activities = {}


def encryption(data):
	return {'message': 'File encrypted successfully'}

def activity_log(data):
	activity = Activity(**data)
	activities[activity.user] = activity
	return {'message': 'Activity logged successfully'}
