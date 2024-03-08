from dataclasses import dataclass

@dataclass
class Activity:
	user: str
	action: str
	timestamp: str

activities = {}


def encrypt_file(data):
	# Placeholder for file encryption
	return {'message': 'File encrypted successfully'}, 201

def activity_log(data):
	activity = Activity(**data)
	activities[activity.timestamp] = activity
	return {'message': 'Activity logged successfully'}, 201
