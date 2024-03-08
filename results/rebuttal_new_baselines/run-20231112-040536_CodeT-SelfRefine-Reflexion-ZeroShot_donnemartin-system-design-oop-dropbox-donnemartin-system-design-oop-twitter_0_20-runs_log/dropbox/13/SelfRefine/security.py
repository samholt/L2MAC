from dataclasses import dataclass

@dataclass
class Activity:
	user_email: str
	action: str

activities = []


def activity_log(data):
	activity = Activity(**data)
	activities.append(activity)
	return {'message': 'Activity logged successfully'}
