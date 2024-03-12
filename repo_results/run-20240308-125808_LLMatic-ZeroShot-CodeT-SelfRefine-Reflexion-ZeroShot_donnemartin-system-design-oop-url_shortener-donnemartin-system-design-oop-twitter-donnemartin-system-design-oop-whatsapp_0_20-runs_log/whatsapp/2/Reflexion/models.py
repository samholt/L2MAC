from dataclasses import dataclass, field
from typing import List

@dataclass
class User:
	id: str
	name: str
	email: str
	password: str
	profile_picture: str = ''
	status_message: str = ''
	contacts: List[str] = field(default_factory=list)
	groups: List[str] = field(default_factory=list)
	blocked_contacts: List[str] = field(default_factory=list)
	last_seen_status: str = 'everyone'

@dataclass
class Group:
	id: str
	name: str
	members: List[str] = field(default_factory=list)
	admins: List[str] = field(default_factory=list)
	group_picture: str = ''
	visible_to: List[str] = field(default_factory=list)
