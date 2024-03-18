# Function to manage statuses
def manage_status(user, status, action, visibility=None):
    # Perform the action
    if action == 'post_status':
        user.post_status(status)
    elif action == 'delete_status':
        user.delete_status(status)
    elif action == 'set_visibility':
        status.set_visibility(visibility)

    # Save the updated status to the database
    # TODO: Add database code here