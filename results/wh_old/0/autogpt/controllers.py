def process_user_request(request):
    pass

def update_model(model, data):
    pass

def send_message(sender, recipients, content, media=None):
    message = Message(sender, recipients, content, media)
    conversation = find_conversation(recipients)
    if not conversation:
        conversation = create_conversation(recipients)
    conversation.add_message(message)
    update_message_status(message, 'delivered')

def find_conversation(participants):
    pass

def create_conversation(participants):
    pass

def create_group_conversation(participants, group_name):
    group_conversation = GroupConversation(participants, group_name)
    return group_conversation

def update_message_status(message, status_type):
    for recipient in message.recipients:
        message.status[recipient][status_type] = True

def mark_message_as_read(message, recipient):
    message.status[recipient]['read'] = True