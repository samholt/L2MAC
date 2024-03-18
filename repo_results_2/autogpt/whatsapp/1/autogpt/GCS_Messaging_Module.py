import os
import datetime

# Message data storage
messages = {}

# Send message function
def send_message(sender_id, recipient_id, content, media=None):
    message_id = os.urandom(16).hex()
    timestamp = datetime.datetime.now()
    messages[message_id] = {
        'sender': sender_id,
        'recipient': recipient_id,
        'content': content,
        'timestamp': timestamp,
        'read': False,
        'media': media
    }
    return 'Message sent successfully.'

# Read message function
def read_message(user_id, message_id):
    if message_id in messages:
        if user_id == messages[message_id]['recipient']:
            messages[message_id]['read'] = True
            return messages[message_id]
        else:
            return 'You are not the recipient of this message.'
    else:
        return 'Message not found.'