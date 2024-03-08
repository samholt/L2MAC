from dataclasses import dataclass


@dataclass
class Contact:
	email: str
	blocked: bool


# Mock database
contacts_db = {}
groups_db = {}


def block_unblock_contact(user_email: str, contact_email: str):
	# Check if contact exists
	if contact_email in contacts_db:
		# Toggle blocked status
		contacts_db[contact_email].blocked = not contacts_db[contact_email].blocked
	else:
		# Create new contact with blocked status
		contacts_db[contact_email] = Contact(contact_email, True)


def create_group(group_name: str, user_email: str):
	# Create new group
	groups_db[group_name] = [user_email]


def edit_group(group_name: str, user_email: str, action: str):
	# Check if group exists
	if group_name in groups_db:
		if action == 'add':
			# Add user to group
			groups_db[group_name].append(user_email)
		elif action == 'remove':
			# Remove user from group
			groups_db[group_name].remove(user_email)

