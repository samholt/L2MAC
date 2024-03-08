import os
from user_auth import register, authenticate
from user_profiles import create_user_profile
from contact_management import create_contact_list
from messaging import create_conversation
from group_chat import create_group_chat
from status_story import create_status_story


def main():
    print('Global Chat Service')
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    user = register(username, password)
    if authenticate(user, password):
        print('Authentication successful')
        display_name = input('Enter your display name: ')
        status = input('Enter your status: ')
        user_profile = create_user_profile(user, display_name, status)
        print(f'User profile created for {user_profile.display_name}')
        contact_list = create_contact_list()
        print('Contact list created')
        conversation = create_conversation(user_profile, None)
        print('Conversation created')
        group_chat = create_group_chat('Test Group')
        print('Group chat created')
        status_story = create_status_story(user_profile, 'My first status', 86400)
        print('Status/story created')
    else:
        print('Authentication failed')


if __name__ == '__main__':
    main()