
# Function to manage group chats
def manage_group_chat(admin, group_chat, action, user=None):
    # Perform the action
    if action == 'add_participant':
        group_chat.add_participant(user)
    elif action == 'remove_participant':
        group_chat.remove_participant(user)

    # Save the updated group chat to the database
    # TODO: Add database code here