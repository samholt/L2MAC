import os
import datetime

# Status/story data storage
statuses = {}

# Post status function
def post_status(user_id, image, visibility):
    status_id = os.urandom(16).hex()
    timestamp = datetime.datetime.now()
    statuses[status_id] = {
        'user': user_id,
        'image': image,
        'timestamp': timestamp,
        'visibility': visibility
    }
    return 'Status posted successfully.'

# View status function
def view_status(user_id, status_id):
    if status_id in statuses:
        if user_id == statuses[status_id]['user'] or (statuses[status_id]['visibility'] == 'everyone' or (statuses[status_id]['visibility'] == 'contacts only' and user_id in contacts[statuses[status_id]['user']])):
            return statuses[status_id]
        else:
            return 'You do not have permission to view this status.'
    else:
        return 'Status not found.'