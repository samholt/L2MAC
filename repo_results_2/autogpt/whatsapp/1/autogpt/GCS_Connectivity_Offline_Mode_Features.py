import os
import datetime

# User data storage
users = {}

# Update online status function
def update_online_status(user_id, online):
    if user_id in users:
        users[user_id]['online'] = online
        if not online:
            users[user_id]['last_seen'] = datetime.datetime.now()
        return 'Online status updated successfully.'
    else:
        return 'User not found.'

# Send message function (updated for offline mode)
def send_message(sender_id, recipient_id, content):
    if sender_id in users and recipient_id in users:
        message_id = os.urandom(16).hex()
        timestamp = datetime.datetime.now()
        message = {
            'id': message_id,
            'sender': sender_id,
            'recipient': recipient_id,
            'content': content,
            'timestamp': timestamp,
            'read': False
        }
        if users[recipient_id]['online']:
            messages[message_id] = message
            return 'Message sent successfully.'
        else:
            users[sender_id]['message_queue'].append(message)
            return 'Recipient is offline. Message queued for delivery.'
    else:
        return 'Sender or recipient not found.'