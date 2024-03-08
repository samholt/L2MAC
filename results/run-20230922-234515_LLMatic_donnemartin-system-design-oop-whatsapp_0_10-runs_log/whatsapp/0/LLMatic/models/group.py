from dataclasses import dataclass

@dataclass
class Group:
	id: int
	name: str
	picture: str
	admin_id: int

@dataclass
class GroupMember:
	group_id: int
	user_id: int
