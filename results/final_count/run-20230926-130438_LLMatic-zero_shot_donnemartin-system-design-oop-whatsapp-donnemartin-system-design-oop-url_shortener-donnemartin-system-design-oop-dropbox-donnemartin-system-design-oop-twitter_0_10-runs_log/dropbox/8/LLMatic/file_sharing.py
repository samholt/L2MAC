from dataclasses import dataclass
from datetime import datetime
from file_management import File, Folder


@dataclass
class ShareableLink:
	url: str
	expiry_date: datetime
	password: str


def generate_link(file_or_folder):
	# Mock implementation of link generation
	if isinstance(file_or_folder, str):
		file_or_folder = File(file_or_folder, '', 0, '', 0, '')
	return ShareableLink(url=f'http://share.com/{file_or_folder.name}', expiry_date=datetime.now(), password='password')


def invite_user(folder: Folder, user):
	folder.shared_users.append(user)

