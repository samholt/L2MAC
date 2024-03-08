from models.group import Group, GroupMember
from utils.database import Database

db = Database()

def create_group(name, picture, admin_id):
	group = Group(None, name, picture, admin_id)
	group.id = db.save_group(group)
	return group

def add_participant(group_id, user_id):
	group_member = GroupMember(group_id, user_id)
	db.save_group_member(group_member)

def remove_participant(group_id, user_id):
	db.delete_group_member(group_id, user_id)

def set_admin(group_id, admin_id):
	group = db.get_group(group_id)
	if group is not None:
		group.admin_id = admin_id
		db.save_group(group)
