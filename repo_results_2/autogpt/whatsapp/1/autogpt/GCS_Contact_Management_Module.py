import os

# Contact and group data storage
contacts = {}
groups = {}

# Block contact function
def block_contact(user_id, contact_id):
    if user_id in contacts:
        if contact_id in contacts[user_id]:
            contacts[user_id].remove(contact_id)
            if 'blocked' in contacts[user_id]:
                contacts[user_id]['blocked'].append(contact_id)
            else:
                contacts[user_id]['blocked'] = [contact_id]
            return 'Contact blocked successfully.'
        else:
            return 'Contact not found.'
    else:
        return 'User not found.'

# Unblock contact function
def unblock_contact(user_id, contact_id):
    if user_id in contacts:
        if 'blocked' in contacts[user_id] and contact_id in contacts[user_id]['blocked']:
            contacts[user_id]['blocked'].remove(contact_id)
            contacts[user_id].append(contact_id)
            return 'Contact unblocked successfully.'
        else:
            return 'Contact not blocked.'
    else:
        return 'User not found.'

# Manage group function
def manage_group(user_id, group_id, action, member_id=None):
    if group_id in groups:
        if action == 'add' and member_id is not None:
            if user_id in groups[group_id]['admins']:
                groups[group_id]['members'].append(member_id)
                return 'Member added successfully.'
            else:
                return 'Only admins can add members.'
        elif action == 'remove' and member_id is not None:
            if user_id in groups[group_id]['admins']:
                if member_id in groups[group_id]['members']:
                    groups[group_id]['members'].remove(member_id)
                    return 'Member removed successfully.'
                else:
                    return 'Member not found.'
            else:
                return 'Only admins can remove members.'
        else:
            return 'Invalid action.'
    else:
        return 'Group not found.'