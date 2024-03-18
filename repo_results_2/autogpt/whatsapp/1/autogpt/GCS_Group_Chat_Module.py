import os

# Group chat data storage
group_chats = {}

# Create group chat function
def create_group_chat(user_id, group_name, group_picture=None):
    group_id = os.urandom(16).hex()
    group_chats[group_id] = {
        'name': group_name,
        'picture': group_picture,
        'admins': [user_id],
        'members': [user_id],
        'messages': []
    }
    return 'Group chat created successfully.'

# Manage group chat function
def manage_group_chat(user_id, group_id, action, member_id=None):
    if group_id in group_chats:
        if action == 'add' and member_id is not None:
            if user_id in group_chats[group_id]['admins']:
                group_chats[group_id]['members'].append(member_id)
                return 'Member added successfully.'
            else:
                return 'Only admins can add members.'
        elif action == 'remove' and member_id is not None:
            if user_id in group_chats[group_id]['admins']:
                if member_id in group_chats[group_id]['members']:
                    group_chats[group_id]['members'].remove(member_id)
                    return 'Member removed successfully.'
                else:
                    return 'Member not found.'
            else:
                return 'Only admins can remove members.'
        elif action == 'promote' and member_id is not None:
            if user_id in group_chats[group_id]['admins']:
                if member_id in group_chats[group_id]['members'] and member_id not in group_chats[group_id]['admins']:
                    group_chats[group_id]['admins'].append(member_id)
                    return 'Member promoted to admin successfully.'
                else:
                    return 'Member not found or already an admin.'
            else:
                return 'Only admins can promote members.'
        else:
            return 'Invalid action.'
    else:
        return 'Group chat not found.'