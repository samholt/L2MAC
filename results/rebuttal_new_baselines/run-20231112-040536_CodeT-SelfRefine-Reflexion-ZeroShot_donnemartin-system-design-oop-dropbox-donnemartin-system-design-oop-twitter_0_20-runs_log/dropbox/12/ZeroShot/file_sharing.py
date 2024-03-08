from dataclasses import dataclass

@dataclass
class Share:
	file_name: str
	user_email: str
	permissions: list

shares = {}


def share_file(data):
	share = Share(**data)
	shares[share.file_name] = share
	return {'status': 'success', 'message': 'File shared successfully'}

def invite_user(data):
	share = shares.get(data['file_name'])
	if share:
		share.user_email = data['user_email']
		return {'status': 'success', 'message': 'User invited successfully'}
	return {'status': 'error', 'message': 'Share not found'}
