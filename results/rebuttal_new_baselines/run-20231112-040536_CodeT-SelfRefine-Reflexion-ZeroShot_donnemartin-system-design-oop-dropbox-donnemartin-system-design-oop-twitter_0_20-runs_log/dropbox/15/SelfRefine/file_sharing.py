from dataclasses import dataclass

@dataclass
class Share:
	file_name: str
	expiry_date: str
	password: str

shares = {}


def share(data):
	share = Share(**data)
	shares[share.file_name] = share
	return {'message': 'File shared successfully'}, 201
