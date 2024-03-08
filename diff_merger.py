import unittest
from summarizer_and_modifier import remove_line_numbers, load_code_files_into_dict
from copy import deepcopy
import re
from collections import Counter
import json
from summarizer_and_modifier import fix_line_spacings, fix_indentation, add_line_numbers
from utils.indenter_utils import reindent_lines

def get_duplicates(lst):
    counts = Counter(lst)
    duplicates = [item for item, count in counts.items() if count > 1]
    return duplicates

def implement_git_diff_on_file_dict(file_dict_input: dict, change_files_and_contents_input: []) -> dict:
    """Implement git diff on file_dict, and return the new file_dict.
    
    Args: file_dict: dict, change_files_and_contents: []

    Returns: dict

    Description: Adheres to this definition: When writing any code you will always give it in diff format, with line numbers. For example. Adding two new lines to a new file is "+ 1: import time\n+ 2: import os". Editing an existing line is "- 5: apple = 2 + 2\n+ 5: apple = 2 + 3". Deleting a line is "- 5: apple = 2 + 2".
    """
    file_dict = deepcopy(file_dict_input)
    change_files_and_contents = deepcopy(change_files_and_contents_input)
    for obj in change_files_and_contents:
        file_path = obj['file_path']
        change_file_contents = obj['file_contents']
        if file_path in file_dict:
            existing_file_contents = file_dict[file_path]
        else:
            existing_file_contents = []
        file_ending = file_path.split('.')[1]
        # new_file_contents = implement_git_diff_on_file_contents(existing_file_contents, change_file_contents, file_type=file_ending, overwrite=obj['overwrite_file'])
        new_file_contents = update_file_contents(existing_file_contents, change_file_contents, file_type=file_ending)
        file_dict[file_path] = new_file_contents
    return file_dict

def update_file_contents(existing_file_contents, change_file_contents, file_type='py') -> [str]:
    """Implement git diff on file_contents, and return the new file_contents.

    Args: existing_file_contents: [str], change_file_contents: [str]

    Returns: [str]

    Description: Adheres to this definition: When writing any code you will always give it in diff format, with line numbers. For example. Adding two new lines to a new file is "+ 1: import time\n+ 2: import os". Editing an existing line is "- 5: apple = 2 + 2\n+ 5: apple = 2 + 3". Deleting a line is "- 5: apple = 2 + 2".
    """
    existing_file_contents = change_file_contents
    return existing_file_contents.split('\n')

# def implement_git_diff_on_file_contents(existing_file_contents, change_file_contents, file_type='py', overwrite=False) -> [str]:
#     """Implement git diff on file_contents, and return the new file_contents.

#     Args: existing_file_contents: [str], change_file_contents: [str]

#     Returns: [str]

#     Description: Adheres to this definition: When writing any code you will always give it in diff format, with line numbers. For example. Adding two new lines to a new file is "+ 1: import time\n+ 2: import os". Editing an existing line is "- 5: apple = 2 + 2\n+ 5: apple = 2 + 3". Deleting a line is "- 5: apple = 2 + 2".
#     """
#     if overwrite:
#         existing_file_contents = []
#     new_file_contents = deepcopy(existing_file_contents)
#     change_file_contents = deepcopy(change_file_contents).replace("\n\n", "§\n")
#     change_file_contents = deepcopy(change_file_contents.strip().split("\n"))
#     existing_file_lns = [int(line.split(':')[0]) for line in new_file_contents]
#     existing_file = {ln: line for ln, line in zip(existing_file_lns, remove_line_numbers(new_file_contents))}
#     buffer_file = deepcopy(existing_file)

#     pattern_extract_diff_lns = re.compile(r'^[+-r]\s*(\d+):')
#     remove_lines = []
#     replace_lines = []
#     add_lines = []
#     for line in change_file_contents:
#         if line:
#             if pattern_extract_diff_lns.match(line):
#                 ln_number = int(pattern_extract_diff_lns.match(line).group(1))
#                 operator = line[0]
#                 if operator == '+':
#                     add_lines.append((ln_number, line))
#                 elif operator == '-':
#                     remove_lines.append(ln_number)
#                 elif operator == 'r':
#                     replace_lines.append((ln_number, line))
#             elif line[0] == '-':
#                 if len(line.split('-')) >= 3:
#                     from_line = int(line.split('-')[1].strip())
#                     to_line = int(line.split('-')[2].strip())
#                     remove_lines.extend(list(range(from_line, to_line+1)))
#                 elif len(line.split('-')) == 2:
#                     remove_lines.append(int(line.split('-')[1].strip()))

#     for remove_ln in remove_lines:
#         if remove_ln in buffer_file:
#             del buffer_file[remove_ln]
    
#     for replace_ln, replace_line in replace_lines:
#         if replace_ln in buffer_file:
#             line = replace_line.split(f'{replace_ln}:')[1]
#             if ' ' in line and line[0] == ' ':
#                 line = line[1:]
#             buffer_file[replace_ln] = line

#     for add_ln, add_line in add_lines:
#         if len(list(existing_file.keys())) == 0:
#             existing_number = 0
#         else:
#             existing_number_max = list(existing_file.keys())[-1]
#             if existing_number_max < add_ln:
#                 existing_number = existing_number_max
#             else:
#                 existing_buffer_lines = [i for i in list(buffer_file.keys()) if i < add_ln]
#                 if len(existing_buffer_lines) == 0:
#                     existing_number = 0
#                 else:
#                     existing_number = [i for i in list(buffer_file.keys()) if i < add_ln][-1]
#         line = add_line.split(f'{add_ln}:')[1]
#         if ' ' in line and line[0] == ' ':
#             line = line[1:]
#         if '.' in str(existing_number):
#             existing_number = int(str(existing_number).split('.')[0])
#         buffer_file[float(f'{existing_number}.{add_ln:03}')] = line
#         buffer_file = dict(sorted(buffer_file.items()))
    
#     buffer_file = dict(sorted(buffer_file.items()))
#     buffer_lines =  list(buffer_file.values())
#     # buffer_lines = '\n'.join(buffer_lines).replace('§','\n').split('\n')
#     # '\n'.join(buffer_lines).replace('§','\n').split('\n')

#     if len(buffer_lines) == 0:
#         buffer_lines = change_file_contents

#     buffer_lines = [line.replace('§','\n') for line in buffer_lines]
#     # if file_type == 'py':
#     #     buffer_lines = fix_line_spacings(buffer_lines)
#     #     buffer_lines = fix_indentation(buffer_lines)
#     #     buffer_lines = reindent_lines(buffer_lines)

#     numbered_lines = add_line_numbers(buffer_lines)
#     return numbered_lines

# def implement_git_diff_on_file_contents_old_version(existing_file_contents, change_file_contents, file_type='py') -> [str]:
#     """Implement git diff on file_contents, and return the new file_contents.

#     Args: existing_file_contents: [str], change_file_contents: [str]

#     Returns: [str]

#     Description: Adheres to this definition: When writing any code you will always give it in diff format, with line numbers. For example. Adding two new lines to a new file is "+ 1: import time\n+ 2: import os". Editing an existing line is "- 5: apple = 2 + 2\n+ 5: apple = 2 + 3". Deleting a line is "- 5: apple = 2 + 2".
#     """
#     new_file_contents = deepcopy(existing_file_contents)
#     change_file_contents = deepcopy(change_file_contents).replace("\n\n", "§\n")
#     change_file_contents = deepcopy(change_file_contents.strip().split("\n"))
#     existing_file_lns = [int(line.split(':')[0]) for line in new_file_contents]
#     existing_file = {ln: line for ln, line in zip(existing_file_lns, remove_line_numbers(new_file_contents))}
#     buffer_file = deepcopy(existing_file)

#     pattern_extract_diff_lns = re.compile(r'^[+-]\s*(\d+):')
#     # change_file_contents_lns = [int(pattern_extract_diff_lns.match(line).group(1)) for line in change_file_contents if pattern_extract_diff_lns.match(line)]
#     previous_line_number = 0
#     change_file_contents_lns = []
#     for line in change_file_contents:
#         if pattern_extract_diff_lns.match(line):
#             ln_number = int(pattern_extract_diff_lns.match(line).group(1))
#         else:
#             ln_number = previous_line_number + 1
#         previous_line_number = ln_number
#         change_file_contents_lns.append(ln_number)
#     assert len(change_file_contents) == len(change_file_contents_lns), "The number of lines in change_file_contents and change_file_contents_lns should be the same."

#     dups = get_duplicates(change_file_contents_lns)
#     for ln_mod, new_line in zip(change_file_contents_lns, change_file_contents):
#         # if not ln_mod in buffer_file and (new_line.startswith("+") or new_line == ''):
#         if (new_line.startswith("+") or new_line == ''):
#             if len(list(existing_file.keys())) == 0:
#                 existing_number = 0
#             else:
#                 existing_number_max = list(existing_file.keys())[-1]
#                 if existing_number_max < ln_mod:
#                     existing_number = existing_number_max
#                 else:
#                     existing_buffer_lines = [i for i in list(buffer_file.keys()) if i < ln_mod]
#                     if len(existing_buffer_lines) == 0:
#                         existing_number = 0
#                     else:
#                         existing_number = [i for i in list(buffer_file.keys()) if i < ln_mod][-1]
#             if new_line != '':
#                 line = new_line.split(f'{ln_mod}:')[1]
#                 if ' ' in line and line[0] == ' ':
#                     line = line[1:]
#                 if ln_mod in dups:
#                     buffer_file[ln_mod] = line
#                 else:
#                     buffer_file[float(f'{existing_number}.{ln_mod:05}')] = line
#                 buffer_file = dict(sorted(buffer_file.items()))
#             else:
#                 buffer_file[float(f'{existing_number}.{ln_mod:05}')] = new_line
#                 buffer_file = dict(sorted(buffer_file.items()))
#         if ln_mod in existing_file and new_line.startswith("-"):
#             del buffer_file[ln_mod]
    
#     buffer_file = dict(sorted(buffer_file.items()))
#     buffer_lines =  list(buffer_file.values())
#     buffer_lines = '\n'.join(buffer_lines).replace('§','\n').split('\n')

#     if file_type == 'py':
#         buffer_lines = fix_line_spacings(buffer_lines)
#         buffer_lines = fix_indentation(buffer_lines)
#         buffer_lines = reindent_lines(buffer_lines)

#     numbered_lines = add_line_numbers(buffer_lines)
#     return numbered_lines

class TestDiffUpdater(unittest.TestCase):
    
    def setUp(self):
        # Create a temporary directory
        code_repository_folder_file_path = "./test_suite/mock_data/chatbot-ui/"
        self.file_dict = load_code_files_into_dict(code_repository_folder_file_path)
        self.test_python_file_dict = {'test-001.py': ['1: import pandas as pd', '2: import os', '3: x = 2 + 5', '4: print(x)']}

    def tearDown(self):
        # Cleanup and remove the temporary directory after test
        pass

    def test_add_files_to_new_file(self):
        file_dict = implement_git_diff_on_file_dict(self.file_dict, [{'file_path': 'test-001.py', 'file_contents': "+ 1: import time\n+ 2: import os"}])
        self.assertEqual(file_dict['test-001.py'], ['1: import time', '2: import os'])

    def test_edit_an_existing_line(self):
        file_dict = implement_git_diff_on_file_dict(self.test_python_file_dict,
                                                    [{'file_path': 'test-001.py', 'file_contents': "- 2: import os\n+ 2: import os.path"}])
        self.assertEqual(file_dict['test-001.py'], ['1: import pandas as pd', '2: import os.path', '3: x = 2 + 5', '4: print(x)'])

    def test_delete_an_existing_lines(self):
        file_dict = implement_git_diff_on_file_dict(self.test_python_file_dict,
                                                    [{'file_path': 'test-001.py', 'file_contents': "- 2: import os\n- 3: x = 2 + 5"}])
        self.assertEqual(file_dict['test-001.py'], ['1: import pandas as pd', '2: print(x)'])


    def test_write_files(self):
        function_args = {'files_and_contents': [{'file_path': 'utils/app/conversation.ts', 'file_contents': "+ 31: export const deleteAllConversations = () => {\n+ 32: localStorage.removeItem('selectedConversation');\n+33: localStorage.removeItem('conversationHistory');\n+ 34: };\n"}, {'file_path': 'components/Promptbar/index.ts', 'file_contents': "+ 2: import { deleteAllConversations } from '@/utils/app/conversation';\n+ 3: \n+ 4: const DeleteChatButton = () => (\n+ 5: <button onClick={deleteAllConversations}>Delete Chat History</button>\n+ 6: )\n+ 7: \n+ 8: export default DeleteChatButton;\n"}]}
        file_dict = implement_git_diff_on_file_dict(self.file_dict, function_args['files_and_contents'])
        
        self.assertEqual(file_dict['utils/app/conversation.ts'],["1: import { Conversation } from '@/types/chat';", '2: ', '3: export const updateConversation = (', '4: updatedConversation: Conversation,', '5: allConversations: Conversation[],', '6: ) => {', '7: const updatedConversations = allConversations.map((c) => {', '8: if (c.id === updatedConversation.id) {', '9: return updatedConversation;', '10: }', '11: ', '12: return c;', '13: });', '14: ', '15: saveConversation(updatedConversation);', '16: saveConversations(updatedConversations);', '17: ', '18: return {', '19: single: updatedConversation,', '20: all: updatedConversations,', '21: };', '22: };', '23: ', '24: export const saveConversation = (conversation: Conversation) => {', "25: localStorage.setItem('selectedConversation', JSON.stringify(conversation));", '26: };', '27: ', '28: export const saveConversations = (conversations: Conversation[]) => {', "29: localStorage.setItem('conversationHistory', JSON.stringify(conversations));", '30: };', '31: export const deleteAllConversations = () => {', "32: localStorage.removeItem('selectedConversation');", "33: localStorage.removeItem('conversationHistory');", '34: };'])
        self.assertEqual(file_dict['components/Promptbar/index.ts'], ["1: export { default } from './Promptbar';", "2: import { deleteAllConversations } from '@/utils/app/conversation';", '3: ', '4: const DeleteChatButton = () => (', '5: <button onClick={deleteAllConversations}>Delete Chat History</button>', '6: )', '7: ', '8: export default DeleteChatButton;'])

    def test_write_files_edge_case_missing_modifier_for_blank_lines(self):
        function_args = {'files_and_contents': [{'file_path': 'main.py', 'file_contents': '+ 1: from user_service import UserService\n+ 2: from chat_service import ChatService\n+ 3: from notifications_service import NotificationService\n+ 4: from message_service import MessageService\n\n+ 6: class ChatApplication:\n+ 7:   """\n+ 8:   Chat Application class.\n+ 9:   It creates and manages instances of user, chat, notification and message services.\n+ 10:   """\n+ 11:   def __init__(self):\n+ 12:     self.user_service = UserService()\n+ 13:     self.chat_service = ChatService()\n+ 14:     self.notification_service = NotificationService()\n+ 15:     self.message_service = MessageService(self.notification_service)\n\n+ 17: # Initialize chat application\n+ 18: app = ChatApplication()'}, {'file_path': 'models.py', 'file_contents': '+ 1: from dataclasses import dataclass\n+ 2: from typing import List\n\n+ 4: @dataclass\n+ 5: class User:\n+ 6:   user_id: str\n+ 7:   is_online: bool\n\n\n+ 9: @dataclass\n+ 10: class Chat:\n+ 11:   chat_id: str\n+ 12:   users: List[User]\n\n\n+ 14: @dataclass\n+ 15: class Message:\n+ 16:   message_id: str\n+ 17:   chat: Chat\n+ 18:   sender: User\n+ 19:   text: str\n+ 20:   media_url: str\n+ 21:   is_read: bool\n+ 22:   is_delivered: bool'}, {'file_path': 'user_service.py', 'file_contents': '+ 1: from models import User\n\n+ 3: class UserService:\n+ 4:   """\n+ 5:   Handles user related functionalities like registration and login\n+ 6:   """\n+ 7:   def register_user(self, user_id: str) -> User:\n+ 8:     """\n+ 9:     Register a new user\n+ 10:     """\n+ 11:     return User(user_id=user_id, is_online=False)\n\n+ 13:   def login_user(self, user: User) -> None:\n+ 14:     """\n+ 15:     User login - sets user status as online\n+ 16:     """\n+ 17:     user.is_online = True\n\n+ 19:   def logout_user(self, user: User) -> None:\n+ 20:     """\n+ 21:     User logout - sets user status as offline\n+ 22:     """\n+ 23:     user.is_online = False'}, {'file_path': 'chat_service.py', 'file_contents': '+ 1: from models import User, Chat\n\n+ 3: class ChatService:\n+ 4:   """\n+ 5:   Handles one-on-one and group chat functionalities\n+ 6:   """\n+ 7:   def create_chat(self, chat_id: str, users: List[User]) -> Chat:\n+ 8:     """\n+ 9:     Create a chat with given users\n+ 10:     """\n+ 11:     return Chat(chat_id=chat_id, users=users)\n\n+ 13:   def add_user_to_chat(self, chat: Chat, user: User) -> None:\n+ 14:     """\n+ 15:     Add a user to a chat\n+ 16:     """\n+ 17:     chat.users.append(user)\n\n+ 19:   def remove_user_from_chat(self, chat: Chat, user: User) -> None:\n+ 20:     """\n+ 21:     Remove a user from a chat\n+ 22:     """\n+ 23:     chat.users.remove(user)'}, {'file_path': 'notifications_service.py', 'file_contents': '+ 1: from models import User\n\n+ 3: class NotificationService:\n+ 4:   """\n+ 5:   Handles push notifications\n+ 6:   """\n+ 7:   def send_push_notification(self, user: User, message_text: str) -> None:\n+ 8:     """\n+ 9:     Send a push notification to the user\n+ 10:     """\n+ 11:     print(f"Sending push notification to {user.user_id} with message: {message_text}")'}, {'file_path': 'message_service.py', 'file_contents': '+ 1: from models import User, Chat, Message\n\n+ 3: class MessageService:\n+ 4:   """\n+ 5:   Handles sending/receiving and reading messages\n+ 6:   """\n+ 7:   def __init__(self, notification_service):\n+ 8:     self.notification_service = notification_service\n\n+ 10:   def send_message(self, chat: Chat, sender: User, receiver: User, message_text: str, media_url=None) -> Message:\n+ 11:     """\n+ 12:     Send a message. Also send push notification to offline users\n+ 13:     """\n+ 14:     message = Message(message_id="id1", chat=chat, sender=sender, text=message_text, media_url=media_url,\n+ 15:                       is_read=False, is_delivered=receiver.is_online)\n\n+ 17:     for user in chat.users:\n+ 18:       if not user.is_online:\n+ 19:         self.notification_service.send_push_notification(user, message_text)\n\n+ 21:     return message\n\n+ 23:  def read_message(self, message: Message) -> None:\n+ 24:     """\n+ 25:     Mark a message as read\n+ 26:     """\n+ 27:     message.is_read = True'}, {'file_path': 'requirements.txt', 'file_contents': '+ 1: dataclasses'}]}

        file_dict = {}
        file_dict = implement_git_diff_on_file_dict(file_dict, function_args['files_and_contents'])
        file_dict_expected = {'main.py': ['1: from user_service import UserService', '2: from chat_service import ChatService', '3: from notifications_service import NotificationService', '4: from message_service import MessageService', '5: ', '6: class ChatApplication:', '7:     """', '8:     Chat Application class.', '9:     It creates and manages instances of user, chat, notification and message services.', '10:     """', '11:     def __init__(self):', '12:         self.user_service = UserService()', '13:         self.chat_service = ChatService()', '14:         self.notification_service = NotificationService()', '15:         self.message_service = MessageService(self.notification_service)', '16: ', '17: # Initialize chat application', '18: app = ChatApplication()'], 'models.py': ['1: from dataclasses import dataclass', '2: from typing import List', '3: ', '4: @dataclass', '5: class User:', '6:     user_id: str', '7:     is_online: bool', '8: ', '9: ', '10: @dataclass', '11: class Chat:', '12:     chat_id: str', '13:     users: List[User]', '14: ', '15: ', '16: @dataclass', '17: class Message:', '18:     message_id: str', '19:     chat: Chat', '20:     sender: User', '21:     text: str', '22:     media_url: str', '23:     is_read: bool', '24:     is_delivered: bool'], 'user_service.py': ['1: from models import User', '2: ', '3: class UserService:', '4:     """', '5:     Handles user related functionalities like registration and login', '6:     """', '7:     def register_user(self, user_id: str) -> User:', '8:         """', '9:         Register a new user', '10:         """', '11:         return User(user_id=user_id, is_online=False)', '12: ', '13:     def login_user(self, user: User) -> None:', '14:         """', '15:         User login - sets user status as online', '16:         """', '17:         user.is_online = True', '18: ', '19:     def logout_user(self, user: User) -> None:', '20:         """', '21:         User logout - sets user status as offline', '22:         """', '23:         user.is_online = False'], 'chat_service.py': ['1: from models import User, Chat', '2: ', '3: class ChatService:', '4:     """', '5:     Handles one-on-one and group chat functionalities', '6:     """', '7:     def create_chat(self, chat_id: str, users: List[User]) -> Chat:', '8:         """', '9:         Create a chat with given users', '10:         """', '11:         return Chat(chat_id=chat_id, users=users)', '12: ', '13:     def add_user_to_chat(self, chat: Chat, user: User) -> None:', '14:         """', '15:         Add a user to a chat', '16:         """', '17:         chat.users.append(user)', '18: ', '19:     def remove_user_from_chat(self, chat: Chat, user: User) -> None:', '20:         """', '21:         Remove a user from a chat', '22:         """', '23:         chat.users.remove(user)'], 'notifications_service.py': ['1: from models import User', '2: ', '3: class NotificationService:', '4:     """', '5:     Handles push notifications', '6:     """', '7:     def send_push_notification(self, user: User, message_text: str) -> None:', '8:         """', '9:         Send a push notification to the user', '10:         """', '11:         print(f"Sending push notification to {user.user_id} with message: {message_text}")'], 'message_service.py': ['1: from models import User, Chat, Message', '2: ', '3: class MessageService:', '4:     """', '5:     Handles sending/receiving and reading messages', '6:     """', '7:     def __init__(self, notification_service):', '8:         self.notification_service = notification_service', '9: ', '10:     def send_message(self, chat: Chat, sender: User, receiver: User, message_text: str, media_url=None) -> Message:', '11:         """', '12:         Send a message. Also send push notification to offline users', '13:         """', '14:         message = Message(message_id="id1", chat=chat, sender=sender, text=message_text, media_url=media_url,', '15:                           is_read=False, is_delivered=receiver.is_online)', '16: ', '17:         for user in chat.users:', '18:             if not user.is_online:', '19:                 self.notification_service.send_push_notification(user, message_text)', '20: ', '21:         return message', '22: ', '23:     def read_message(self, message: Message) -> None:', '24:         """', '25:         Mark a message as read', '26:         """', '27:         message.is_read = True'], 'requirements.txt': ['1: dataclasses']}

        self.assertEqual(file_dict['message_service.py'], file_dict_expected['message_service.py'])

        for key in file_dict.keys():
            self.assertEqual(file_dict[key], file_dict_expected[key])

    def test_write_files_edge_case_missing_exception_0(self):
        function_args = {'files_and_contents': [{'file_path': 'chat_service.py', 'file_contents': "+ 1: from dataclasses import dataclass\n+ 2: import time\n+ 3: from abc import ABC, abstractmethod\n+ 4:\n+ 5: STATUS_SENT = 'sent'\n+ 6: STATUS_DELIVERED = 'delivered'\n+ 7: STATUS_READ = 'read'\n+ 8:\n+ 9: @dataclass\n+10: class User:\n+11:     user_id: str\n+12:     username: str\n+13:     connected: bool = True\n+14:\n+15: @dataclass\n+16: class Message:\n+17:     message_id: str\n+18:     sender: User\n+19:     receiver: User\n+20:     sent_time: float\n+21:     delivered_time: float = None\n+22:     read_time: float = None\n+23:     status: str = STATUS_SENT\n+24:\n+25:     def delivered(self):\n+26:         self.status = STATUS_DELIVERED\n+27:         self.delivered_time = time.time()\n+28:\n+29:     def read(self):\n+30:         self.status = STATUS_READ\n+31:         self.read_time = time.time()\n+32:\n+33: @dataclass\n+34: class Group:\n+35:     group_id: str\n+36:     users: list\n+37:     messages: list = None\n+38:\n+39:     def add_user(self, user):\n+40:         if user not in self.users:\n+41:             self.users.append(user)\n+42:\n+43:     def remove_user(self, user):\n+44:         if user in self.users:\n+45:             self.users.remove(user)\n+46:\n+47: class Messenger(ABC):\n+48:     @abstractmethod\n+49:     def send_message(self, sender, receiver, message):\n+50:         pass"}, {'file_path': 'notification_service.py', 'file_contents': "+ 1: class NotificationService:\n+ 2:     def send(self, user, message):\n+ 3:         if user.connected:\n+ 4:             print(f'Notification sent to {user.username} for message: {message.message_id}')"}, {'file_path': 'encryption_service.py', 'file_contents': '+ 1: class EncryptionService:\n+ 2:     def __init__(self, encryption_key):\n+ 3:         self.encryption_key = encryption_key\n+ 4:\n+ 5:     def encrypt(self, message):\n+ 6:         # Implement your preferred encryption method here\n+ 7:         return message\n+ 8:\n+ 9:     def decrypt(self, encrypted_message):\n+10:         # Implement your preferred decryption method here\n+11:         return encrypted_message'}, {'file_path': 'db_service.py', 'file_contents': '+ 1: class DbService:\n+ 2:     def __init__(self):\n+ 3:         self.users = []\n+ 4:         self.messages = []\n+ 5:         self.groups = []\n+ 6:\n+ 7:     def save_message(self, message):\n+ 8:         self.messages.append(message)\n+ 9:\n+10:     def save_user(self, user):\n+11:         self.users.append(user)\n+12:\n+13:     def save_group(self, group):\n+14:         self.groups.append(group)\n+15:     def get_user(self, user_id):\n+16:         user = [user for user in self.users if user.user_id == user_id]\n+17:         return user[0] if user else None\n+18:\n+19:     def get_messages_for_user(self, user_id):\n+20:         messages = [message for message in self.messages if message.receiver.user_id == user_id]\n+21:         return messages\n+22:\n+23:     def get_group(self, group_id):\n+24:         group = [group for group in this.groups if group.group_id == group_id]\n+25:         return group[0] if group else None\n+26:\n+27:     def get_messages_for_group(self, group_id):\n+28:         messages = [message for message in self.messages if isinstance(message.receiver, Group) and message.receiver.group_id == group_id]\n+29:         return messages'}, {'file_path': 'test_chat_service.py', 'file_contents': '+ 1: import pytest\n+ 2: from chat_service import ChatService, User, Message\n+ 3:\n+ 4: # Define your test cases here'}, {'file_path': 'requirements.txt', 'file_contents': '+ 1: pytest==6.2.5'}]}

        file_dict = {}
        file_dict = implement_git_diff_on_file_dict(file_dict, function_args['files_and_contents'])
        self.assertEqual(file_dict, {'chat_service.py': ['1: from dataclasses import dataclass', '2: import time', '3: from abc import ABC, abstractmethod', '4: ', "5: STATUS_SENT = 'sent'", "6: STATUS_DELIVERED = 'delivered'", "7: STATUS_READ = 'read'", '8: ', '9: @dataclass', '10: class User:', '11:     user_id: str', '12:     username: str', '13:     connected: bool = True', '14: ', '15: @dataclass', '16: class Message:', '17:     message_id: str', '18:     sender: User', '19:     receiver: User', '20:     sent_time: float', '21:     delivered_time: float = None', '22:     read_time: float = None', '23:     status: str = STATUS_SENT', '24: ', '25:     def delivered(self):', '26:         self.status = STATUS_DELIVERED', '27:         self.delivered_time = time.time()', '28: ', '29:     def read(self):', '30:         self.status = STATUS_READ', '31:         self.read_time = time.time()', '32: ', '33: @dataclass', '34: class Group:', '35:     group_id: str', '36:     users: list', '37:     messages: list = None', '38: ', '39:     def add_user(self, user):', '40:         if user not in self.users:', '41:             self.users.append(user)', '42: ', '43:     def remove_user(self, user):', '44:         if user in self.users:', '45:             self.users.remove(user)', '46: ', '47: class Messenger(ABC):', '48:     @abstractmethod', '49:     def send_message(self, sender, receiver, message):', '50:         pass'], 'notification_service.py': ['1: class NotificationService:', '2:     def send(self, user, message):', '3:         if user.connected:', "4:             print(f'Notification sent to {user.username} for message: {message.message_id}')"], 'encryption_service.py': ['1: class EncryptionService:', '2:     def __init__(self, encryption_key):', '3:         self.encryption_key = encryption_key', '4: ', '5:     def encrypt(self, message):', '6:         # Implement your preferred encryption method here', '7:         return message', '8: ', '9:     def decrypt(self, encrypted_message):', '10:         # Implement your preferred decryption method here', '11:         return encrypted_message'], 'db_service.py': ['1: class DbService:', '2:     def __init__(self):', '3:         self.users = []', '4:         self.messages = []', '5:         self.groups = []', '6: ', '7:     def save_message(self, message):', '8:         self.messages.append(message)', '9: ', '10:     def save_user(self, user):', '11:         self.users.append(user)', '12: ', '13:     def save_group(self, group):', '14:         self.groups.append(group)', '15:     def get_user(self, user_id):', '16:         user = [user for user in self.users if user.user_id == user_id]', '17:         return user[0] if user else None', '18: ', '19:     def get_messages_for_user(self, user_id):', '20:         messages = [message for message in self.messages if message.receiver.user_id == user_id]', '21:         return messages', '22: ', '23:     def get_group(self, group_id):', '24:         group = [group for group in this.groups if group.group_id == group_id]', '25:         return group[0] if group else None', '26: ', '27:     def get_messages_for_group(self, group_id):', '28:         messages = [message for message in self.messages if isinstance(message.receiver, Group) and message.receiver.group_id == group_id]', '29:         return messages'], 'test_chat_service.py': ['1: import pytest', '2: from chat_service import ChatService, User, Message', '3: ', '4: # Define your test cases here'], 'requirements.txt': ['1: pytest==6.2.5']})


    def test_double_delete_and_add_corner_case(self):
        file_dict = {'vehicle.py': ['1: class Vehicle:', '2:     def __init__(self, license_plate: str, spot_size: str):', '3:         self.license_plate = license_plate', '4:         self.spot_size = spot_size', '5:         self.is_parked = False', '6:     def park(self):', '7:         self.is_parked = True', '8:     def remove(self):', '9:         self.is_parked = False'], 'motorcycle.py': ['1: from vehicle import Vehicle', '2: ', '3: class Motorcycle(Vehicle):', '4:     def __init__(self, license_plate: str):', "5:         super().__init__(license_plate, 'small')"], 'car.py': ['1: from vehicle import Vehicle', '2: ', '3: class Car(Vehicle):', '4:     def __init__(self, license_plate: str):', "5:         super().__init__(license_plate, 'compact')"], 'bus.py': ['1: from vehicle import Vehicle', '2: ', '3: class Bus(Vehicle):', '4:     def __init__(self, license_plate: str):', "5:         super().__init__(license_plate, 'large')"], 'parking_spot.py': ['1: class ParkingSpot:', '2:     def __init__(self, spot_id: int, spot_size: str):', '3:         self.spot_id = spot_id', '4:         self.spot_size = spot_size', '5:         self.is_occupied = False', '6:     def park(self):', '7:         self.is_occupied = True', '8:     def remove(self):', '9:         self.is_occupied = False'], 'parking_lot.py': ['1: from parking_spot import ParkingSpot', '2: ', '3: class ParkingLot:', '4:     def __init__(self, total_spots: int):', '5:         self.total_spots = total_spots', '6:         self.available_spots = total_spots', "7:         self.spots = [ParkingSpot(i, 'large') for i in range(total_spots)]", '8: ', '9:     def park(self, vehicle):', '10:         if self.is_full():', "11:             raise Exception('Parking lot is full')", '12:         for spot in self.spots:', '13:             if not spot.is_occupied and spot.spot_size == vehicle.spot_size:', '14:                 spot.park()', '15:                 vehicle.park()', '16:                 self.available_spots -= 1', '17:                 break', '18: ', '19:     def remove(self, vehicle):', '20:         for spot in self.spots:', '21:             if spot.is_occupied and spot.spot_size == vehicle.spot_size:', '22:                 spot.remove()', '23:                 vehicle.remove()', '24:                 self.available_spots += 1', '25:                 break', '26: ', '27:     def is_full(self):', '28:         return self.available_spots == 0'], 'level.py': ['1: from parking_spot import ParkingSpot', '2: ', '3: class Level:', '4:     def __init__(self, level_id: int, total_spots: int):', '5:         self.level_id = level_id', '6:         self.total_spots = total_spots', '7:         self.available_spots = total_spots', "8:         self.spots = [ParkingSpot(i, 'large') for i in range(total_spots)]", '9: ', '10:     def park(self):', '11:         if self.is_full():', '12:             raise Exception("Parking level is full")', '13:         for spot in self.spots:', '14:             if not spot.is_occupied:', '15:                 spot.park()', '16:                 self.available_spots -= 1', '17:                 return', '18:         raise Exception("No available spots")', '19: ', '20:     def remove(self):', '21:         for spot in self.spots:', '22:             if spot.is_occupied:', '23:                 spot.remove()', '24:                 self.available_spots += 1', '25:                 return', '26:         raise Exception("No occupied spots")', '27: ', '28:     def is_full(self):', '29:         return self.available_spots == 0'], 'parking_lot_system.py': ['1: from level import Level', '2: ', '3: class ParkingLotSystem:', '4:     def __init__(self, total_levels: int, spots_per_level: int):', '5:         self.total_levels = total_levels', '6:         self.levels = [Level(i, spots_per_level) for i in range(total_levels)]', '7: ', '8:     def park(self, vehicle):', '9:         for level in self.levels:', '10:             if not level.is_full():', '11:                 level.park(vehicle)', '12:                 return', "13:         raise Exception('Parking lot is full')"], 'test_parking_lot_system.py': ['1: import pytest', '2: from vehicle import Vehicle', '3: from motorcycle import Motorcycle', '4: from car import Car', '5: from bus import Bus', '6: from parking_spot import ParkingSpot', '7: from parking_lot import ParkingLot', '8: from level import Level', '9: from parking_lot_system import ParkingLotSystem', '10: ', '11: def test_vehicle():', "12:     vehicle = Vehicle('123', 'large')", "13:     assert vehicle.license_plate == '123'", "14:     assert vehicle.spot_size == 'large'", '15:     assert vehicle.is_parked == False', '16:     vehicle.park()', '17:     assert vehicle.is_parked == True', '18:     vehicle.remove()', '19:     assert vehicle.is_parked == False', '20: ', '21: def test_motorcycle():', "22:     motorcycle = Motorcycle('123')", "23:     assert motorcycle.license_plate == '123'", "24:     assert motorcycle.spot_size == 'small'", '25:     assert motorcycle.is_parked == False', '26: ', '27: def test_car():', "28:     car = Car('123')", "29:     assert car.license_plate == '123'", "30:     assert car.spot_size == 'compact'", '31:     assert car.is_parked == False', '32: ', '33: def test_bus():', "34:     bus = Bus('123')", "35:     assert bus.license_plate == '123'", "36:     assert bus.spot_size == 'large'", '37:     assert bus.is_parked == False', '38: ', '39: def test_parking_spot():', "40:     spot = ParkingSpot(1, 'large')", '41:     assert spot.spot_id == 1', "42:     assert spot.spot_size == 'large'", '43:     assert spot.is_occupied == False', '44:     spot.park()', '45:     assert spot.is_occupied == True', '46:     spot.remove()', '47:     assert spot.is_occupied == False', '48: ', '49: def test_parking_lot():', '50:     lot = ParkingLot(10)', '51:     assert lot.total_spots == 10', '52:     assert lot.available_spots == 10', '53:     assert len(lot.spots) == 10', "54:     vehicle = Vehicle('123', 'large')", '55:     lot.park(vehicle)', '56:     assert lot.available_spots == 9', '57:     lot.remove(vehicle)', '58:     assert lot.available_spots == 10', '59:     with pytest.raises(Exception):', '60:         for _ in range(11):', '61:             lot.park(vehicle)', '62: ', '63: def test_level():', '64:     level = Level(1, 10)', '65:     assert level.level_id == 1', '66:     assert level.total_spots == 10', '67:     assert level.available_spots == 10', '68:     assert len(level.spots) == 10', "69:     vehicle = Vehicle('123', 'large')", '70:     level.park(vehicle)', '71:     assert level.available_spots == 9', '72:     level.remove(vehicle)', '73:     assert level.available_spots == 10', '74:     with pytest.raises(Exception):', '75:         for _ in range(11):', '76:             level.park(vehicle)', '77: ', '78: def test_parking_lot_system():', '79:     system = ParkingLotSystem(2, 10)', '80:     assert system.total_levels == 2', '81:     assert len(system.levels) == 2', "82:     vehicle = Vehicle('123', 'large')", '83:     system.park(vehicle)', '84:     assert system.levels[0].available_spots == 9', '85:     with pytest.raises(Exception):', '86:         for _ in range(21):', '87:             system.park(vehicle)'], 'requirements.txt': ['1: pytest']}

        files_and_contents = [{'file_path': 'level.py', 'file_contents': '- 10:     def park(self):\n+ 10:     def park(self, vehicle):\n- 20:     def remove(self):\n+ 20:     def remove(self, vehicle):'}, {'file_path': 'parking_lot_system.py', 'file_contents': '- 8:     def park(self, vehicle):\n+ 8:     def park(self, vehicle):\n- 11:                 level.park(vehicle)\n+ 11:                 level.park(vehicle):'}]

        file_dict = implement_git_diff_on_file_dict(file_dict, files_and_contents)
        expected_level_py = ['1: from parking_spot import ParkingSpot', '2: ', '3: class Level:', '4:     def __init__(self, level_id: int, total_spots: int):', '5:         self.level_id = level_id', '6:         self.total_spots = total_spots', '7:         self.available_spots = total_spots', "8:         self.spots = [ParkingSpot(i, 'large') for i in range(total_spots)]", '9: ', '10:     def park(self, vehicle):', '11:         if self.is_full():', '12:             raise Exception("Parking level is full")', '13:         for spot in self.spots:', '14:             if not spot.is_occupied:', '15:                 spot.park()', '16:                 self.available_spots -= 1', '17:                 return', '18:         raise Exception("No available spots")', '19: ', '20:     def remove(self, vehicle):', '21:         for spot in self.spots:', '22:             if spot.is_occupied:', '23:                 spot.remove()', '24:                 self.available_spots += 1', '25:                 return', '26:         raise Exception("No occupied spots")', '27: ', '28:     def is_full(self):', '29:         return self.available_spots == 0']
        self.assertEqual(file_dict['level.py'], expected_level_py) 

    def test_more_replacements(self):
        existing_file_contents = ['1: from level import Level', '2: ', '3: class ParkingLotSystem:', '4:     def __init__(self, total_levels: int, spots_per_level: int):', '5:         self.total_levels = total_levels', '6:         self.levels = [Level(i, spots_per_level) for i in range(total_levels)]', '7: ', '8:     def park(self, vehicle):', '9:         for level in self.levels:', '10:             if not level.is_full():', '11:                 level.park(vehicle)', '12:                 return', "13:         raise Exception('Parking lot is full')"]
        change_file_contents = '- 8:     def park(self, vehicle):\n+ 8:     def park(self):\n- 9:         for level in self.levels:\n+ 9:         for level in self.levels:\n- 10:             if not level.is_full():\n+ 10:             if not level.is_full():\n- 11:                 level.park(vehicle)\n+ 11:                 level.park()'
        new_file_contents = implement_git_diff_on_file_contents(existing_file_contents, change_file_contents)
        self.assertEqual(new_file_contents, ['1: from level import Level', '2: ', '3: class ParkingLotSystem:', '4:     def __init__(self, total_levels: int, spots_per_level: int):', '5:         self.total_levels = total_levels', '6:         self.levels = [Level(i, spots_per_level) for i in range(total_levels)]', '7: ', '8:     def park(self):', '9:         for level in self.levels:', '10:             if not level.is_full():', '11:                 level.park()', '12:                 return', "13:         raise Exception('Parking lot is full')"])


    def test_line_indentation_fix(self):
        with open('./examples/parking_executing_main_indent_issues.json', 'r') as fh:
            data = json.load(fh)
        file_dict = data['file_dict']
        change_file_contents = "- 34: def can_fit_vehicle(self, vehicle: Vehicle):\n+ 34:     def can_fit_vehicle(self, vehicle: Vehicle):"
        existing_file_contents = file_dict['parking_spot.py']
        new_file_contents = implement_git_diff_on_file_contents(existing_file_contents, change_file_contents)
        print('')

    def test_line_indentation_fix_redux(self):
        existing_file_contents = [] 

        change_file_contents = "+ 1: from typing import List\n+ 2: from level import Level\n\n+ 3: class ParkingLot:\n+ 4:     def __init__(self, num_levels: int):\n+ 5:         self.levels: List[Level] = []\n+ 6:         for i in range(num_levels):\n+ 7:             self.levels.append(Level(i, 30))\n\n+ 8:     def park_vehicle(self, vehicle):\n+ 9:         for level in self.levels:\n+ 10:             if level.is_spot_available() and level.park_vehicle(vehicle):\n+ 11:                 return True\n+ 12:         return False\n\n+ 13:     def unpark_vehicle(self, vehicle):\n+ 14:         for level in self.levels:\n+ 15:             if level.unpark_vehicle(vehicle):\n+ 16:                 return True\n+ 17:         return False"
        new_file_contents = implement_git_diff_on_file_contents(existing_file_contents, change_file_contents)
        self.assertEqual(new_file_contents, ['1: from typing import List', '2: from level import Level', '3: ', '4: class ParkingLot:', '5:     def __init__(self, num_levels: int):', '6:         self.levels: List[Level] = []', '7:         for i in range(num_levels):', '8:             self.levels.append(Level(i, 30))', '9: ', '10:     def park_vehicle(self, vehicle):', '11:         for level in self.levels:', '12:             if level.is_spot_available() and level.park_vehicle(vehicle):', '13:                 return True', '14:         return False', '15: ', '16:     def unpark_vehicle(self, vehicle):', '17:         for level in self.levels:', '18:             if level.unpark_vehicle(vehicle):', '19:                 return True', '20:         return False'])

    def test_more_nuanced_identation(self):
        change_file_contents = '+ 1: from models import User, Chat, Message\n\n+ 3: class MessageService:\n+ 4:   """\n+ 5:   Handles sending/receiving and reading messages\n+ 6:   """\n+ 7:   def __init__(self, notification_service):\n+ 8:     self.notification_service = notification_service\n\n+ 10:   def send_message(self, chat: Chat, sender: User, receiver: User, message_text: str, media_url=None) -> Message:\n+ 11:     """\n+ 12:     Send a message. Also send push notification to offline users\n+ 13:     """\n+ 14:     message = Message(message_id="id1", chat=chat, sender=sender, text=message_text, media_url=media_url,\n+ 15:                       is_read=False, is_delivered=receiver.is_online)\n\n+ 17:     for user in chat.users:\n+ 18:       if not user.is_online:\n+ 19:         self.notification_service.send_push_notification(user, message_text)\n\n+ 21:     return message\n\n+ 23:  def read_message(self, message: Message) -> None:\n+ 24:     """\n+ 25:     Mark a message as read\n+ 26:     """\n+ 27:     message.is_read = True'
        existing_file_contents = []
        new_file_contents = implement_git_diff_on_file_contents(existing_file_contents, change_file_contents)
        expected = ['1: from models import User, Chat, Message', '2: ', '3: class MessageService:', '4:     """', '5:     Handles sending/receiving and reading messages', '6:     """', '7:     def __init__(self, notification_service):', '8:         self.notification_service = notification_service', '9: ', '10:     def send_message(self, chat: Chat, sender: User, receiver: User, message_text: str, media_url=None) -> Message:', '11:         """', '12:         Send a message. Also send push notification to offline users', '13:         """', '14:         message = Message(message_id="id1", chat=chat, sender=sender, text=message_text, media_url=media_url,', '15:                           is_read=False, is_delivered=receiver.is_online)', '16: ', '17:         for user in chat.users:', '18:             if not user.is_online:', '19:                 self.notification_service.send_push_notification(user, message_text)', '20: ', '21:         return message', '22: ', '23:     def read_message(self, message: Message) -> None:', '24:         """', '25:         Mark a message as read', '26:         """', '27:         message.is_read = True']
        self.assertEqual(new_file_contents, expected)

    def test_corner_case_replace_then_add(self):
        change_file_contents = "- 31:     def is_spot_available(self):\n+ 31:     @property\n+ 32:     def is_available(self):\n33:         return self.is_available"
        existing_file_string = """1: from enum import Enum
2: from vehicle import Vehicle, VehicleSize
3: 
4: class SpotSize(Enum):
5:     MOTORCYCLE = 1
6:     COMPACT = 2
7:     LARGE = 3
8: 
9: class ParkingSpot:
10:     def __init__(self, spot_id: str, spot_size: SpotSize, level_id: int):
11:         self.spot_id = spot_id
12:         self.spot_size = spot_size
13:         self.level_id = level_id
14:         self.is_available = True
15:         self.vehicle = None
16: 
17:     def park_vehicle(self, vehicle: Vehicle):
18:         if self.is_available and self.can_fit_vehicle(vehicle):
19:             self.vehicle = vehicle
20:             self.is_available = False
21:             return True
22:         return False
23: 
24:     def unpark_vehicle(self):
25:         if not self.is_available:
26:             self.vehicle = None
27:             self.is_available = True
28:             return True
29:         return False
30: 
31:     def is_spot_available(self):
32:         return self.is_available
33: 
34:     def can_fit_vehicle(self, vehicle: Vehicle):
35:         if vehicle.get_size() == VehicleSize.MOTORCYCLE:
36:             return True
37:         elif vehicle.get_size() == VehicleSize.COMPACT and self.spot_size != SpotSize.MOTORCYCLE:
38:             return True
39:         elif vehicle.get_size() == VehicleSize.LARGE and self.spot_size == SpotSize.LARGE:
40:             return True
41:         return False"""
        existing_file_contents = existing_file_string.split('\n')
        new_file_contents = implement_git_diff_on_file_contents(existing_file_contents, change_file_contents)
        self.assertEqual(new_file_contents, ['1: from enum import Enum', '2: from vehicle import Vehicle, VehicleSize', '3: ', '4: class SpotSize(Enum):', '5:     MOTORCYCLE = 1', '6:     COMPACT = 2', '7:     LARGE = 3', '8: ', '9: class ParkingSpot:', '10:     def __init__(self, spot_id: str, spot_size: SpotSize, level_id: int):', '11:         self.spot_id = spot_id', '12:         self.spot_size = spot_size', '13:         self.level_id = level_id', '14:         self.is_available = True', '15:         self.vehicle = None', '16: ', '17:     def park_vehicle(self, vehicle: Vehicle):', '18:         if self.is_available and self.can_fit_vehicle(vehicle):', '19:             self.vehicle = vehicle', '20:             self.is_available = False', '21:             return True', '22:         return False', '23: ', '24:     def unpark_vehicle(self):', '25:         if not self.is_available:', '26:             self.vehicle = None', '27:             self.is_available = True', '28:             return True', '29:         return False', '30: ', '31:     @property', '32:     def is_available(self):', '33:         return self.is_available', '34: ', '35:     def can_fit_vehicle(self, vehicle: Vehicle):', '36:         if vehicle.get_size() == VehicleSize.MOTORCYCLE:', '37:             return True', '38:         elif vehicle.get_size() == VehicleSize.COMPACT and self.spot_size != SpotSize.MOTORCYCLE:', '39:             return True', '40:         elif vehicle.get_size() == VehicleSize.LARGE and self.spot_size == SpotSize.LARGE:', '41:             return True', '42:         return False'])

    def test_corner_case_replace_then_replace(self):
        change_file_contents = 'r 9:     def park_vehicles(self, vehicle):\nr 24:     def remove_vehicle_all_the_way(self, vehicle):'
        existing_file_string = """1: from parking_spot import MotorcycleSpot, CompactSpot, LargeSpot
2: from vehicle import Vehicle, VehicleSize
3: 
4: class Level:
5:     def __init__(self, spots):
6:         self.spots = {MotorcycleSpot: spots['MotorcycleSpot'], CompactSpot: spots['CompactSpot'], LargeSpot: spots['LargeSpot']}
7:         self.available_spots = {MotorcycleSpot: spots['MotorcycleSpot'], CompactSpot: spots['CompactSpot'], LargeSpot: spots['LargeSpot']}
8: 
9:     def park_vehicle(self, vehicle):
10:         if isinstance(vehicle, Motorcycle):
11:             if self.available_spots[MotorcycleSpot] > 0:
12:                 self.available_spots[MotorcycleSpot] -= 1
13:                 return True
14:         elif isinstance(vehicle, Car):
15:             if self.available_spots[CompactSpot] > 0:
16:                 self.available_spots[CompactSpot] -= 1
17:                 return True
18:         elif isinstance(vehicle, Bus):
19:             if self.available_spots[LargeSpot] >= 5:
20:                 self.available_spots[LargeSpot] -= 5
21:                 return True
22:         return False
23: 
24:     def remove_vehicle(self, vehicle):
25:         if isinstance(vehicle, Motorcycle):
26:             self.available_spots[MotorcycleSpot] += 1
27:             return True
28:         elif isinstance(vehicle, Car):
29:             self.available_spots[CompactSpot] += 1
30:             return True
31:         elif isinstance(vehicle, Bus):
32:             self.available_spots[LargeSpot] += 5
33:             return True
34:         return False"""
        existing_file_contents = existing_file_string.split('\n')
        new_file_contents = implement_git_diff_on_file_contents(existing_file_contents, change_file_contents)
        expected_file = """1: from parking_spot import MotorcycleSpot, CompactSpot, LargeSpot
2: from vehicle import Vehicle, VehicleSize
3: 
4: class Level:
5:     def __init__(self, spots):
6:         self.spots = {MotorcycleSpot: spots['MotorcycleSpot'], CompactSpot: spots['CompactSpot'], LargeSpot: spots['LargeSpot']}
7:         self.available_spots = {MotorcycleSpot: spots['MotorcycleSpot'], CompactSpot: spots['CompactSpot'], LargeSpot: spots['LargeSpot']}
8: 
9:     def park_vehicles(self, vehicle):
10:         if isinstance(vehicle, Motorcycle):
11:             if self.available_spots[MotorcycleSpot] > 0:
12:                 self.available_spots[MotorcycleSpot] -= 1
13:                 return True
14:         elif isinstance(vehicle, Car):
15:             if self.available_spots[CompactSpot] > 0:
16:                 self.available_spots[CompactSpot] -= 1
17:                 return True
18:         elif isinstance(vehicle, Bus):
19:             if self.available_spots[LargeSpot] >= 5:
20:                 self.available_spots[LargeSpot] -= 5
21:                 return True
22:         return False
23: 
24:     def remove_vehicle_all_the_way(self, vehicle):
25:         if isinstance(vehicle, Motorcycle):
26:             self.available_spots[MotorcycleSpot] += 1
27:             return True
28:         elif isinstance(vehicle, Car):
29:             self.available_spots[CompactSpot] += 1
30:             return True
31:         elif isinstance(vehicle, Bus):
32:             self.available_spots[LargeSpot] += 5
33:             return True
34:         return False"""
        self.assertEqual(new_file_contents, expected_file.split('\n'))

    def test_removing_line_indentation_corner_case(self):
        change_file_contents = "- 27:   class Supervisor(Employee):\n+ 27: class Supervisor(Employee):"
        existing_file_contents = ['1: class Employee:', '2:     def __init__(self, name, level):', '3:         self.name = name', '4:         self.level = level', '5:         self.available = True', '6: ', '7:     def handle_call(self, call):', '8:         raise NotImplementedError', '9: ', '10:     def escalate_call(self, call):', '11:         raise NotImplementedError', '12: ', '13:     def is_available(self):', '14:         return self.available', '15: ', '16: class Operator(Employee):', '17:     def __init__(self, name):', "18:         super().__init__(name, 'Operator')", '19: ', '20:     def handle_call(self, call):', '21:         self.available = False', '22:         # Implement specific behavior for Operator', '23: ', '24:     def escalate_call(self, call):', '25:         # Implement specific behavior for Operator', '26: ', '27:   class Supervisor(Employee):', '28:     def __init__(self, name):', "29:         super().__init__(name, 'Supervisor')", '30: ', '31:     def handle_call(self, call):', '32:         self.available = False', '33:         # Implement specific behavior for Supervisor', '34: ', '35:     def escalate_call(self, call):', '36:         # Implement specific behavior for Supervisor', '37: ', '38: class Director(Employee):', '39:     def __init__(self, name):', "40:         super().__init__(name, 'Director')", '41: ', '42:     def handle_call(self, call):', '43:         self.available = False', '44:         # Implement specific behavior for Director', '45: ', '46:     def escalate_call(self, call):', '47:         # Implement specific behavior for Director']
        new_file_contents = implement_git_diff_on_file_contents(existing_file_contents, change_file_contents)
        self.assertEqual(new_file_contents, ['1: class Employee:', '2:     def __init__(self, name, level):', '3:         self.name = name', '4:         self.level = level', '5:         self.available = True', '6: ', '7:     def handle_call(self, call):', '8:         raise NotImplementedError', '9: ', '10:     def escalate_call(self, call):', '11:         raise NotImplementedError', '12: ', '13:     def is_available(self):', '14:         return self.available', '15: ', '16: class Operator(Employee):', '17:     def __init__(self, name):', "18:         super().__init__(name, 'Operator')", '19: ', '20:     def handle_call(self, call):', '21:         self.available = False', '22:         # Implement specific behavior for Operator', '23: ', '24:     def escalate_call(self, call):', '25:         # Implement specific behavior for Operator', '26: ', '27: class Supervisor(Employee):', '28:     def __init__(self, name):', "29:         super().__init__(name, 'Supervisor')", '30: ', '31:     def handle_call(self, call):', '32:         self.available = False', '33:         # Implement specific behavior for Supervisor', '34: ', '35:     def escalate_call(self, call):', '36:         # Implement specific behavior for Supervisor', '37: ', '38: class Director(Employee):', '39:     def __init__(self, name):', "40:         super().__init__(name, 'Director')", '41: ', '42:     def handle_call(self, call):', '43:         self.available = False', '44:         # Implement specific behavior for Director', '45: ', '46:     def escalate_call(self, call):', '47:         # Implement specific behavior for Director'])

    def test_complete_removal_and_re_adding_of_file(self):
        change_file_contents = ['- 1: from typing import Dict', '- 2: from vehicle import Vehicle', '- 3: ', '- 4: class Level:', '- 5:     def __init__(self, level_number: int, spot_count: int):', '- 6:         self.level_number = level_number', '- 7:         self.spot_count = spot_count', '- 8:         self.spots = [None]*spot_count', '- 9:         self.available_spots = spot_count', '- 10: ', '- 11:     def park_vehicle(self, vehicle: Vehicle) -> bool:', '- 12:         if self.available_spots > 0:', '- 13:             for i in range(self.spot_count):', '- 14:                 if self.spots[i] is None:', '- 15:                     self.spots[i] = vehicle', '- 16:                     self.available_spots -= 1', '- 17:                     return True', '- 18:         return False', '- 19: ', '- 20:     def remove_vehicle(self, vehicle: Vehicle) -> bool:', '- 21:         for i in range(self.spot_count):', '- 22:             if self.spots[i] == vehicle:', '- 23:                 self.spots[i] = None', '- 24:                 self.available_spots += 1', '- 25:                 return True', '- 26:         return False', '+ 1: from typing import Dict', '+ 2: from vehicle import Vehicle', '+ 3: ', '+ 4: class Level:', '+ 5:     def __init__(self, level_number: int, spots: Dict[str, int]):', '+ 6:         self.level_number = level_number', '+ 7:         self.spots = {spot_type: [None]*count for spot_type, count in spots.items()}', '+ 8:         self.available_spots = {spot_type: count for spot_type, count in spots.items()}', '+ 9: ', '+ 10:     def park_vehicle(self, vehicle: Vehicle) -> bool:', '+ 11:         for spot_type, spots in self.spots.items():', '+ 12:             if issubclass(vehicle.size, spot_type) and self.available_spots[spot_type] > 0:', '+ 13:                 for i in range(len(spots)):', '+ 14:                     if spots[i] is None:', '+ 15:                         spots[i] = vehicle', '+ 16:                         self.available_spots[spot_type] -= 1', '+ 17:                         return True', '+ 18:         return False', '+ 19: ', '+ 20:     def remove_vehicle(self, vehicle: Vehicle) -> bool:', '+ 21:         for spot_type, spots in self.spots.items():', '+ 22:             for i in range(len(spots)):', '+ 23:                 if spots[i] == vehicle:', '+ 24:                     spots[i] = None', '+ 25:                     self.available_spots[spot_type] += 1', '+ 26:                     return True', '+ 27:         return False']
        existing_file_contents = ['1: from typing import Dict, List', '2: from vehicle import Vehicle', '3: from parking_spot import ParkingSpot, MotorcycleSpot, CompactSpot, LargeSpot', '4: ', '5: class Level:', '6:     def __init__(self, level_number: int, spot_count: Dict[str, int]):', '7:         self.level_number = level_number', '8:         self.spots = {}', '9:         self.available_spots = {}', '10:         for spot_type, count in spot_count.items():', '11:             self.spots[spot_type] = [self._create_spot(spot_type, i) for i in range(count)]', '12:             self.available_spots[spot_type] = count', '13: ', '14:     def _create_spot(self, spot_type: str, spot_number: int) -> ParkingSpot:', "15:         if spot_type == 'MotorcycleSpot':", '16:             return MotorcycleSpot(str(spot_number), self.level_number)', "17:         elif spot_type == 'CompactSpot':", '18:             return CompactSpot(str(spot_number), self.level_number)', "19:         elif spot_type == 'LargeSpot':", '20:             return LargeSpot(str(spot_number), self.level_number)', '21: ', '22:     def park_vehicle(self, vehicle: Vehicle) -> bool:', '23:         for spot_type in self.spots:', '24:             for spot in self.spots[spot_type]:', '25:                 if spot.is_available() and spot.park(vehicle):', '26:                     self.available_spots[spot_type] -= 1', '27:                     return True', '28:         return False', '29: ', '30:     def remove_vehicle(self, vehicle: Vehicle) -> bool:', '31:         for spot_type in self.spots:', '32:             for spot in self.spots[spot_type]:', '33:                 if spot.vehicle == vehicle:', '34:                     spot.remove_vehicle()', '35:                     self.available_spots[spot_type] += 1', '36:                     return True', '37:         return False', '38: ', '39:     def is_full(self) -> bool:', '40:         return all(count == 0 for count in self.available_spots.values())']
        change_file_contents = '\n'.join(change_file_contents)
        new_file_contents = implement_git_diff_on_file_contents(existing_file_contents, change_file_contents)
        self.assertEqual(new_file_contents, ['1: from typing import Dict', '2: from vehicle import Vehicle', '3: ', '4: class Level:', '5:     def __init__(self, level_number: int, spots: Dict[str, int]):', '6:         self.level_number = level_number', '7:         self.spots = {spot_type: [None]*count for spot_type, count in spots.items()}', '8:         self.available_spots = {spot_type: count for spot_type, count in spots.items()}', '9: ', '10:     def park_vehicle(self, vehicle: Vehicle) -> bool:', '11:         for spot_type, spots in self.spots.items():', '12:             if issubclass(vehicle.size, spot_type) and self.available_spots[spot_type] > 0:', '13:                 for i in range(len(spots)):', '14:                     if spots[i] is None:', '15:                         spots[i] = vehicle', '16:                         self.available_spots[spot_type] -= 1', '17:                         return True', '18:         return False', '19: ', '20:     def remove_vehicle(self, vehicle: Vehicle) -> bool:', '21:         for spot_type, spots in self.spots.items():', '22:             for i in range(len(spots)):', '23:                 if spots[i] == vehicle:', '24:                     spots[i] = None', '25:                     self.available_spots[spot_type] += 1', '26:                     return True', '27:         return False', '28:             return True', '29:         return False', '30: ', '31:     def remove_vehicle(self, vehicle: Vehicle) -> bool:', '32:         for spot_type in self.spots:', '33:             for spot in self.spots[spot_type]:', '34:                 if spot.vehicle == vehicle:', '35:                     spot.remove_vehicle()', '36:                     self.available_spots[spot_type] += 1', '37:                     return True', '38:         return False', '39: ', '40:     def is_full(self) -> bool:', '41:         return all(count == 0 for count in self.available_spots.values())'])


    def fundamental_test_needs_parse_raising_potentially_limited_understanding_of_llm_using_tools(self):
        # If consistently fails with this failure mode, may have to break the task into more meaningful subtasks, where the output encoding is correct.
        # Or give the code an automatic way to correct itself.
        # Or call an LLM to verify the output. I.e. have a probabilistic measure of if it is completed correctly, then iterate on this.
        # change_file_contents_from_LLMatic = "+ 1: from vehicle import Motorcycle, Car, Bus\n+ 2: \n+ 3: class Level:\n+ 4:     def __init__(self, spots):\n+ 5:         self.spots = spots\n+ 6:         self.available_spots = {k: v for k, v in spots.items()}\n+ 7: \n+ 8:     def park_vehicle(self, vehicle):\n+ 9:         if isinstance(vehicle, Motorcycle):\n+ 10:             if self.available_spots['MotorcycleSpot'] > 0:\n+ 11:                 self.available_spots['MotorcycleSpot'] -= 1\n+ 12:                 return True\n+ 13:             elif self.available_spots['CompactSpot'] > 0:\n+ 14:                 self.available_spots['CompactSpot'] -= 1\n+ 15:                 return True\n+ 16:             elif self.available_spots['LargeSpot'] > 0:\n+ 17:                 self.available_spots['LargeSpot'] -= 1\n+ 18:                 return True\n+ 19:         elif isinstance(vehicle, Car):\n+ 20:             if self.available_spots['CompactSpot'] > 0:\n+ 21:                 self.available_spots['CompactSpot'] -= 1\n+ 22:                 return True\n+ 23:             elif self.available_spots['LargeSpot'] > 0:\n+ 24:                 self.available_spots['LargeSpot'] -= 1\n+ 25:                 return True\n+ 26:         elif isinstance(vehicle, Bus):\n+ 27:             if self.available_spots['LargeSpot'] >= 5:\n+ 28:                 self.available_spots['LargeSpot'] -= 5\n+ 29:                 return True\n+ 30:         return False\n+ 31: \n+ 32:     def remove_vehicle(self, vehicle):\n+ 33:         if isinstance(vehicle, Motorcycle):\n+ 34:             if self.spots['MotorcycleSpot'] > self.available_spots['MotorcycleSpot']:\n+ 35:                 self.available_spots['MotorcycleSpot'] += 1\n+ 36:                 return True\n+ 37:             elif self.spots['CompactSpot'] > self.available_spots['CompactSpot']:\n+ 38:                 self.available_spots['CompactSpot'] += 1\n+ 39:                 return True\n+ 40:             elif self.spots['LargeSpot'] > self.available_spots['LargeSpot']:\n+ 41:                 self.available_spots['LargeSpot'] += 1\n+ 42:                 return True\n+ 43:         elif isinstance(vehicle, Car):\n+ 44:             if self.spots['CompactSpot'] > self.available_spots['CompactSpot']:\n+ 45:                 self.available_spots['CompactSpot'] += 1\n+ 46:                 return True\n+ 47:             elif self.spots['LargeSpot'] > self.available_spots['LargeSpot']:\n+ 48:                 self.available_spots['LargeSpot'] += 1\n+ 49:                 return True\n+ 50:         elif isinstance(vehicle, Bus):\n+ 51:             if self.spots['LargeSpot'] - 5 >= self.available_spots['LargeSpot']:\n+ 52:                 self.available_spots['LargeSpot'] += 5\n+ 53:                 return True\n+ 54:         return False"
        # change_file_contents_from_test_bot = "- 1: from parking_spot import MotorcycleSpot, CompactSpot, LargeSpot\n- 2: from vehicle import Vehicle, VehicleSize\n+ 1: from vehicle import Motorcycle, Car, Bus\n- 4: class Level:\n- 5:     def __init__(self, spots):\n- 6:         self.spots = {MotorcycleSpot: spots['MotorcycleSpot'], CompactSpot: spots['CompactSpot'], LargeSpot: spots['LargeSpot']}\n- 7:         self.available_spots = {MotorcycleSpot: spots['MotorcycleSpot'], CompactSpot: spots['CompactSpot'], LargeSpot: spots['LargeSpot']}\n+ 4: class Level:\n+ 5:     def __init__(self, spots):\n+ 6:         self.spots = spots\n+ 7:         self.available_spots = {k: v for k, v in spots.items()}\n- 9:     def park_vehicle(self, vehicle):\n- 10:         if isinstance(vehicle, Motorcycle):\n- 11:             if self.available_spots[MotorcycleSpot] > 0:\n- 12:                 self.available_spots[MotorcycleSpot] -= 1\n- 13:                 return True\n- 14:         elif isinstance(vehicle, Car):\n- 15:             if self.available_spots[CompactSpot] > 0:\n- 16:                 self.available_spots[CompactSpot] -= 1\n- 17:                 return True\n- 18:         elif isinstance(vehicle, Bus):\n- 19:             if self.available_spots[LargeSpot] >= 5:\n- 20:                 self.available_spots[LargeSpot] -= 5\n- 21:                 return True\n- 22:         return False\n+ 8:     def park_vehicle(self, vehicle):\n+ 9:         if isinstance(vehicle, Motorcycle):\n+ 10:             if self.available_spots['MotorcycleSpot'] > 0:\n+ 11:                 self.available_spots['MotorcycleSpot'] -= 1\n+ 12:                 return True\n+ 13:             elif self.available_spots['CompactSpot'] > 0:\n+ 14:                 self.available_spots['CompactSpot'] -= 1\n+ 15:                 return True\n+ 16:             elif self.available_spots['LargeSpot'] > 0:\n+ 17:                 self.available_spots['LargeSpot'] -= 1\n+ 18:                 return True\n+ 19:         elif isinstance(vehicle, Car):\n+ 20:             if self.available_spots['CompactSpot'] > 0:\n+ 21:                 self.available_spots['CompactSpot'] -= 1\n+ 22:                 return True\n+ 23:             elif self.available_spots['LargeSpot'] > 0:\n+ 24:                 self.available_spots['LargeSpot'] -= 1\n+ 25:                 return True\n+ 26:         elif isinstance(vehicle, Bus):\n+ 27:             if self.available_spots['LargeSpot'] >= 5:\n+ 28:                 self.available_spots['LargeSpot'] -= 5\n+ 29:                 return True\n+ 30:         return False\n- 24:     def remove_vehicle(self, vehicle):\n- 25:         if isinstance(vehicle, Motorcycle):\n- 26:             self.available_spots[MotorcycleSpot] += 1\n- 27:             return True\n- 28:         elif isinstance(vehicle, Car):\n- 29:             self.available_spots[CompactSpot] += 1\n- 30:             return True\n- 31:         elif isinstance(vehicle, Bus):\n- 32:             self.available_spots[LargeSpot] += 5\n- 33:             return True\n- 34:         return False\n+ 32:     def remove_vehicle(self, vehicle):\n+ 33:         if isinstance(vehicle, Motorcycle):\n+ 34:             if self.spots['MotorcycleSpot'] > self.available_spots['MotorcycleSpot']:\n+ 35:                 self.available_spots['MotorcycleSpot'] += 1\n+ 36:                 return True\n+ 37:             elif self.spots['CompactSpot'] > self.available_spots['CompactSpot']:\n+ 38:                 self.available_spots['CompactSpot'] += 1\n+ 39:                 return True\n+ 40:             elif self.spots['LargeSpot'] > self.available_spots['LargeSpot']:\n+ 41:                 self.available_spots['LargeSpot'] += 1\n+ 42:                 return True\n+ 43:         elif isinstance(vehicle, Car):\n+ 44:             if self.spots['CompactSpot'] > self.available_spots['CompactSpot']:\n+ 45:                 self.available_spots['CompactSpot'] += 1\n+ 46:                 return True\n+ 47:             elif self.spots['LargeSpot'] > self.available_spots['LargeSpot']:\n+ 48:                 self.available_spots['LargeSpot'] += 1\n+ 49:                 return True\n+ 50:         elif isinstance(vehicle, Bus):\n+ 51:             if self.spots['LargeSpot'] - 5 >= self.available_spots['LargeSpot']:\n+ 52:                 self.available_spots['LargeSpot'] += 5\n+ 53:                 return True\n+ 54:         return False"
        existing_file_contents = ['1: from parking_spot import MotorcycleSpot, CompactSpot, LargeSpot', '2: from vehicle import Vehicle, VehicleSize', '3: ', '4: class Level:', '5:     def __init__(self, spots):', "6:         self.spots = {MotorcycleSpot: spots['MotorcycleSpot'], CompactSpot: spots['CompactSpot'], LargeSpot: spots['LargeSpot']}", "7:         self.available_spots = {MotorcycleSpot: spots['MotorcycleSpot'], CompactSpot: spots['CompactSpot'], LargeSpot: spots['LargeSpot']}", '8: ', '9:     def park_vehicle(self, vehicle):', '10:         if isinstance(vehicle, Motorcycle):', '11:             if self.available_spots[MotorcycleSpot] > 0:', '12:                 self.available_spots[MotorcycleSpot] -= 1', '13:                 return True', '14:         elif isinstance(vehicle, Car):', '15:             if self.available_spots[CompactSpot] > 0:', '16:                 self.available_spots[CompactSpot] -= 1', '17:                 return True', '18:         elif isinstance(vehicle, Bus):', '19:             if self.available_spots[LargeSpot] >= 5:', '20:                 self.available_spots[LargeSpot] -= 5', '21:                 return True', '22:         return False', '23: ', '24:     def remove_vehicle(self, vehicle):', '25:         if isinstance(vehicle, Motorcycle):', '26:             self.available_spots[MotorcycleSpot] += 1', '27:             return True', '28:         elif isinstance(vehicle, Car):', '29:             self.available_spots[CompactSpot] += 1', '30:             return True', '31:         elif isinstance(vehicle, Bus):', '32:             self.available_spots[LargeSpot] += 5', '33:             return True', '34:         return False']
        change_file_contents_from_test_bot = "- 1-34\n+ 1: from vehicle import Motorcycle, Car, Bus\n+ 2: \n+ 3: class Level:\n+ 4:     def __init__(self, spots):\n+ 5:         self.spots = spots\n+ 6:         self.available_spots = {k: v for k, v in spots.items()}\n+ 7: \n+ 8:     def park_vehicle(self, vehicle):\n+ 9:         if isinstance(vehicle, Motorcycle):\n+ 10:             if self.available_spots['MotorcycleSpot'] > 0:\n+ 11:                 self.available_spots['MotorcycleSpot'] -= 1\n+ 12:                 return True\n+ 13:             elif self.available_spots['CompactSpot'] > 0:\n+ 14:                 self.available_spots['CompactSpot'] -= 1\n+ 15:                 return True\n+ 16:             elif self.available_spots['LargeSpot'] > 0:\n+ 17:                 self.available_spots['LargeSpot'] -= 1\n+ 18:                 return True\n+ 19:         elif isinstance(vehicle, Car):\n+ 20:             if self.available_spots['CompactSpot'] > 0:\n+ 21:                 self.available_spots['CompactSpot'] -= 1\n+ 22:                 return True\n+ 23:             elif self.available_spots['LargeSpot'] > 0:\n+ 24:                 self.available_spots['LargeSpot'] -= 1\n+ 25:                 return True\n+ 26:         elif isinstance(vehicle, Bus):\n+ 27:             if self.available_spots['LargeSpot'] >= 5:\n+ 28:                 self.available_spots['LargeSpot'] -= 5\n+ 29:                 return True\n+ 30:         return False\n+ 31: \n+ 32:     def remove_vehicle(self, vehicle):\n+ 33:         if isinstance(vehicle, Motorcycle):\n+ 34:             if self.spots['MotorcycleSpot'] > self.available_spots['MotorcycleSpot']:\n+ 35:                 self.available_spots['MotorcycleSpot'] += 1\n+ 36:                 return True\n+ 37:             elif self.spots['CompactSpot'] > self.available_spots['CompactSpot']:\n+ 38:                 self.available_spots['CompactSpot'] += 1\n+ 39:                 return True\n+ 40:             elif self.spots['LargeSpot'] > self.available_spots['LargeSpot']:\n+ 41:                 self.available_spots['LargeSpot'] += 1\n+ 42:                 return True\n+ 43:         elif isinstance(vehicle, Car):\n+ 44:             if self.spots['CompactSpot'] > self.available_spots['CompactSpot']:\n+ 45:                 self.available_spots['CompactSpot'] += 1\n+ 46:                 return True\n+ 47:             elif self.spots['LargeSpot'] > self.available_spots['LargeSpot']:\n+ 48:                 self.available_spots['LargeSpot'] += 1\n+ 49:                 return True\n+ 50:         elif isinstance(vehicle, Bus):\n+ 51:             if self.spots['LargeSpot'] - 5 >= self.available_spots['LargeSpot']:\n+ 52:                 self.available_spots['LargeSpot'] += 5\n+ 53:                 return True\n+ 54:         return False"
        new_file_contents = implement_git_diff_on_file_contents(existing_file_contents, change_file_contents_from_test_bot)
        self.assertEqual(new_file_contents, ['1: from vehicle import Motorcycle, Car, Bus', '2: ', '3: class Level:', '4:     def __init__(self, spots):', '5:         self.spots = spots', '6:         self.available_spots = {k: v for k, v in spots.items()}', '7: ', '8:     def park_vehicle(self, vehicle):', '9:         if isinstance(vehicle, Motorcycle):', "10:             if self.available_spots['MotorcycleSpot'] > 0:", "11:                 self.available_spots['MotorcycleSpot'] -= 1", '12:                 return True', "13:             elif self.available_spots['CompactSpot'] > 0:", "14:                 self.available_spots['CompactSpot'] -= 1", '15:                 return True', "16:             elif self.available_spots['LargeSpot'] > 0:", "17:                 self.available_spots['LargeSpot'] -= 1", '18:                 return True', '19:         elif isinstance(vehicle, Car):', "20:             if self.available_spots['CompactSpot'] > 0:", "21:                 self.available_spots['CompactSpot'] -= 1", '22:                 return True', "23:             elif self.available_spots['LargeSpot'] > 0:", "24:                 self.available_spots['LargeSpot'] -= 1", '25:                 return True', '26:         elif isinstance(vehicle, Bus):', "27:             if self.available_spots['LargeSpot'] >= 5:", "28:                 self.available_spots['LargeSpot'] -= 5", '29:                 return True', '30:         return False', '31: ', '32:     def remove_vehicle(self, vehicle):', '33:         if isinstance(vehicle, Motorcycle):', "34:             if self.spots['MotorcycleSpot'] > self.available_spots['MotorcycleSpot']:", "35:                 self.available_spots['MotorcycleSpot'] += 1", '36:                 return True', "37:             elif self.spots['CompactSpot'] > self.available_spots['CompactSpot']:", "38:                 self.available_spots['CompactSpot'] += 1", '39:                 return True', "40:             elif self.spots['LargeSpot'] > self.available_spots['LargeSpot']:", "41:                 self.available_spots['LargeSpot'] += 1", '42:                 return True', '43:         elif isinstance(vehicle, Car):', "44:             if self.spots['CompactSpot'] > self.available_spots['CompactSpot']:", "45:                 self.available_spots['CompactSpot'] += 1", '46:                 return True', "47:             elif self.spots['LargeSpot'] > self.available_spots['LargeSpot']:", "48:                 self.available_spots['LargeSpot'] += 1", '49:                 return True', '50:         elif isinstance(vehicle, Bus):', "51:             if self.spots['LargeSpot'] - 5 >= self.available_spots['LargeSpot']:", "52:                 self.available_spots['LargeSpot'] += 5", '53:                 return True', '54:         return False'])


    def fundamental_test_needs_parse_raising_other_fine_case(self):
        existing_file_contents = ['1: from parking_spot import MotorcycleSpot, CompactSpot, LargeSpot', '2: from vehicle import Vehicle, VehicleSize', '3: ', '4: class Level:', '5:     def __init__(self, spots):', "6:         self.spots = {MotorcycleSpot: spots['MotorcycleSpot'], CompactSpot: spots['CompactSpot'], LargeSpot: spots['LargeSpot']}", "7:         self.available_spots = {MotorcycleSpot: spots['MotorcycleSpot'], CompactSpot: spots['CompactSpot'], LargeSpot: spots['LargeSpot']}", '8: ', '9:     def park_vehicle(self, vehicle):', '10:         if isinstance(vehicle, Motorcycle):', '11:             if self.available_spots[MotorcycleSpot] > 0:', '12:                 self.available_spots[MotorcycleSpot] -= 1', '13:                 return True', '14:         elif isinstance(vehicle, Car):', '15:             if self.available_spots[CompactSpot] > 0:', '16:                 self.available_spots[CompactSpot] -= 1', '17:                 return True', '18:         elif isinstance(vehicle, Bus):', '19:             if self.available_spots[LargeSpot] >= 5:', '20:                 self.available_spots[LargeSpot] -= 5', '21:                 return True', '22:         return False', '23: ', '24:     def remove_vehicle(self, vehicle):', '25:         if isinstance(vehicle, Motorcycle):', '26:             self.available_spots[MotorcycleSpot] += 1', '27:             return True', '28:         elif isinstance(vehicle, Car):', '29:             self.available_spots[CompactSpot] += 1', '30:             return True', '31:         elif isinstance(vehicle, Bus):', '32:             self.available_spots[LargeSpot] += 5', '33:             return True', '34:         return False']
        
        change_file_contents_from_test_bot = '- 9\n- 24\n+ 9:     def park_vehicles(self, vehicle):\n+ 24:     def remove_vehicle_all_the_way(self, vehicle):'
        new_file_contents = implement_git_diff_on_file_contents(existing_file_contents, change_file_contents_from_test_bot)
        self.assertEqual(new_file_contents, ['1: from parking_spot import MotorcycleSpot, CompactSpot, LargeSpot', '2: from vehicle import Vehicle, VehicleSize', '3: ', '4: class Level:', '5:     def __init__(self, spots):', "6:         self.spots = {MotorcycleSpot: spots['MotorcycleSpot'], CompactSpot: spots['CompactSpot'], LargeSpot: spots['LargeSpot']}", "7:         self.available_spots = {MotorcycleSpot: spots['MotorcycleSpot'], CompactSpot: spots['CompactSpot'], LargeSpot: spots['LargeSpot']}", '8: ', '9:     def park_vehicles(self, vehicle):', '10:         if isinstance(vehicle, Motorcycle):', '11:             if self.available_spots[MotorcycleSpot] > 0:', '12:                 self.available_spots[MotorcycleSpot] -= 1', '13:                 return True', '14:         elif isinstance(vehicle, Car):', '15:             if self.available_spots[CompactSpot] > 0:', '16:                 self.available_spots[CompactSpot] -= 1', '17:                 return True', '18:         elif isinstance(vehicle, Bus):', '19:             if self.available_spots[LargeSpot] >= 5:', '20:                 self.available_spots[LargeSpot] -= 5', '21:                 return True', '22:         return False', '23: ', '24:     def remove_vehicle_all_the_way(self, vehicle):', '25:         if isinstance(vehicle, Motorcycle):', '26:             self.available_spots[MotorcycleSpot] += 1', '27:             return True', '28:         elif isinstance(vehicle, Car):', '29:             self.available_spots[CompactSpot] += 1', '30:             return True', '31:         elif isinstance(vehicle, Bus):', '32:             self.available_spots[LargeSpot] += 5', '33:             return True', '34:         return False'])

    def test_fundamental_corruption_case(self):
        file_dict = {'main.py': ['1: from flask import Flask', '2: from views import url_shortener', '3: from models import Base, engine\n', '4: def create_app():', '5:     app = Flask(__name__)', '6:     app.register_blueprint(url_shortener)', '7:     Base.metadata.create_all(bind=engine)', '8:     return app\n', "9: if __name__ == '__main__':", '10:     app = create_app()', '11:     app.run(debug=True)'], 'models.py': ['1: from datetime import datetime', '2: from sqlalchemy import Column, Integer, String, DateTime', '3: from sqlalchemy.ext.declarative import declarative_base\n', '4: Base = declarative_base()\n', '5: class URL(Base):', "6:     __tablename__ = 'urls'", '7:     id = Column(Integer, primary_key=True)', '8:     original_url = Column(String, nullable=False)', '9:     short_url = Column(String, nullable=False, unique=True)', '10:     created_at = Column(DateTime, default=datetime.utcnow)', '11:     expires_at = Column(DateTime)', '12:     click_count = Column(Integer, default=0)'], 'views.py': ['1: from flask import Blueprint, request, redirect', '2: from .controllers import create_short_url, get_original_url, delete_expired_urls\n', "3: url_shortener = Blueprint('url_shortener', __name__)\n", "4: @url_shortener.route('/shorten', methods=['POST'])", '5: def shorten_url():', "6:     original_url = request.json.get('original_url')", "7:     custom_alias = request.json.get('custom_alias')", '8:     short_url = create_short_url(original_url, custom_alias)', "9:     return {'short_url': short_url}, 201\n", "10: @url_shortener.route('/<string:short_url>', methods=['GET'])", '11: def redirect_to_original(short_url):', '12:     original_url = get_original_url(short_url)', '13:     if original_url:', '14:         return redirect(original_url)', '15:     else:', "16:         return {'error': 'URL not found'}, 404\n", "17: @url_shortener.route('/expired', methods=['DELETE'])", '18: def remove_expired():', '19:     delete_expired_urls()', '20:     return {}, 204'], 'controllers.py': ['1: from models import URL, db', '2: import string', '3: import random', '4: from datetime import datetime, timedelta\n', '5: def generate_short_url(length=6):', '6:     # Generate a random string of the given length', "7:     return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))\n", '8: def create_short_url(original_url, custom_alias=None):', '9:     # If a custom alias is provided, use it as the short URL', '10:     short_url = custom_alias if custom_alias else generate_short_url()', '11:     # Create a new URL object and save it to the database', '12:     url = URL(original_url=original_url, short_url=short_url, creation_date=datetime.now(), expiration_date=datetime.now() + timedelta(days=30), click_count=0)', '13:     db.session.add(url)', '14:     db.session.commit()', '15:     return url\n', '16: def get_original_url(short_url):', '17:     # Find the URL object by the short URL', '18:     url = URL.query.filter_by(short_url=short_url).first()', '19:     return url\n', '20: def increment_click_count(url):', '21:     # Increment the click count of the given URL object', '22:     url.click_count += 1', '23:     db.session.commit()\n', '24: def delete_expired_urls():', '25:     # Find all URL objects that have expired and delete them', '26:     expired_urls = URL.query.filter(URL.expiration_date < datetime.now()).all()', '27:     for url in expired_urls:', '28:         db.session.delete(url)', '29:     db.session.commit()'], 'tests.py': ['1: import pytest', '2: from controllers import create_short_url, get_original_url, increment_click_count, delete_expired_urls', '3: from models import URL, db', '4: from datetime import datetime, timedelta\n', '5: def test_create_short_url():', "6:     original_url = 'https://www.example.com'", '7:     short_url = create_short_url(original_url)', '8:     assert short_url.original_url == original_url', '9:     assert len(short_url.short_url) == 6\n', '10: def test_create_short_url_with_custom_alias():', "11:     original_url = 'https://www.example.com'", "12:     custom_alias = 'custom'", '13:     short_url = create_short_url(original_url, custom_alias)', '14:     assert short_url.original_url == original_url', '15:     assert short_url.short_url == custom_alias\n', '16: def test_get_original_url():', "17:     original_url = 'https://www.example.com'", '18:     short_url = create_short_url(original_url)', '19:     retrieved_url = get_original_url(short_url.short_url)', '20:     assert retrieved_url.original_url == original_url\n', '21: def test_increment_click_count():', "22:     original_url = 'https://www.example.com'", '23:     short_url = create_short_url(original_url)', '24:     increment_click_count(short_url)', '25:     assert short_url.click_count == 1\n', '26: def test_delete_expired_urls():', "27:     original_url = 'https://www.example.com'", '28:     short_url = create_short_url(original_url)', '29:     short_url.expires_at = datetime.now() - timedelta(days=1)', '30:     db.session.commit()', '31:     delete_expired_urls()', '32:     assert URL.query.get(short_url.id) is None'], 'requirements.txt': ['1: Flask', '2: SQLAlchemy', '3: pytest']}
        files_and_contents = [{'file_path': 'models.py', 'file_contents': "+ 1: from flask_sqlalchemy import SQLAlchemy\n+ 2: db = SQLAlchemy()\n- 3-12\n+ 3: from datetime import datetime\n+ 4: from sqlalchemy import Column, Integer, String, DateTime\n+ 5: from sqlalchemy.ext.declarative import declarative_base\n\n+ 6: Base = declarative_base()\n\n+ 7: class URL(Base):\n+ 8:     __tablename__ = 'urls'\n+ 9:     id = Column(Integer, primary_key=True)\n+ 10:     original_url = Column(String, nullable=False)\n+ 11:     short_url = Column(String, nullable=False, unique=True)\n+ 12:     created_at = Column(DateTime, default=datetime.utcnow)\n+ 13:     expires_at = Column(DateTime)\n+ 14:     click_count = Column(Integer, default=0)"}, {'file_path': 'main.py', 'file_contents': "+ 1: from flask import Flask\n+ 2: from models import db\n\n+ 3: app = Flask(__name__)\n+ 4: app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'\n+ 5: db.init_app(app)\n\n+ 6: import views\n+ 7: app.register_blueprint(views.bp)\n\n+ 8: if __name__ == '__main__':\n+ 9:     app.run(debug=True)"}]
        file_dict = implement_git_diff_on_file_dict(file_dict, files_and_contents)

    def test_over_writing_files(self):
        files_and_contents = [{'file_path': 'message.py', 'file_contents': '+ 1: from cryptography.fernet import Fernet\n+ 2: \n+ 3: class Message:\n+ 4:     def __init__(self, id, sender, receiver, content):\n+ 5:         self.id = id\n+ 6:         self.sender = sender\n+ 7:         self.receiver = receiver\n+ 8:         self.content = self.encrypt_message(content)\n+ 9:         self.timestamp = datetime.datetime.now()\n+ 10:         self.delivered = False\n+ 11:         self.read = False\n+ 12: \n+ 13:     def encrypt_message(self, message):\n+ 14:         key = Fernet.generate_key()\n+ 15:         cipher_suite = Fernet(key)\n+ 16:         cipher_text = cipher_suite.encrypt(message.encode())\n+ 17:         return cipher_text\n+ 18: \n+ 19:     def decrypt_message(self):\n+ 20:         key = Fernet.generate_key()\n+ 21:         cipher_suite = Fernet(key)\n+ 22:         plain_text = cipher_suite.decrypt(self.content).decode()\n+ 23:         return plain_text\n+ 24: \n+ 25:     def mark_as_delivered(self):\n+ 26:         self.delivered = True\n+ 27: \n+ 28:     def mark_as_read(self):\n+ 29:         self.read = True\n+ 30:         self.content = self.decrypt_message()', 'overwrite_file': True}, {'file_path': 'user.py', 'file_contents': '+ 7:     def send_message(self, chat_id, content):\n+ 8:         for chat in self.chats:\n+ 9:             if chat.id == chat_id:\n+ 10:                 chat.add_message(self.id, content)\n+ 11:                 break\n+ 12: \n+ 13:     def read_message(self, chat_id, message_id):\n+ 14:         for chat in self.chats:\n+ 15:             if chat.id == chat_id:\n+ 16:                 message = chat.get_message(message_id)\n+ 17:                 if message:\n+ 18:                     message.mark_as_read()\n+ 19:                     return message.decrypt_message()\n+ 20:                 break\n+ 21:         return None', 'overwrite_file': False}]
        file_dict = {'user.py': ['1: class User:', '2:     def __init__(self, id, name):', '3:         self.id = id', '4:         self.name = name', '5:         self.chats = []', '6: ', '7:     def send_message(self, chat_id, content):', '8:         for chat in self.chats:', '9:             if chat.id == chat_id:', '10:                 chat.add_message(self.id, content)', '11:                 break', '12: ', '13:     def read_message(self, chat_id, message_id):', '14:         for chat in self.chats:', '15:             if chat.id == chat_id:', '16:                 message = chat.get_message(message_id)', '17:                 if message:', '18:                     message.mark_as_read()', '19:                 break', '20: ', '21:     def get_status(self, chat_id, message_id):', '22:         for chat in self.chats:', '23:             if chat.id == chat_id:', '24:                 message = chat.get_message(message_id)', '25:                 if message:', '26:                     return message.delivered, message.read', '27:                 break', '28:         return None, None'], 'message.py': ['1: import datetime', '2: ', '3: class Message:', '4:     def __init__(self, id, sender, receiver, content):', '5:         self.id = id', '6:         self.sender = sender', '7:         self.receiver = receiver', '8:         self.content = content', '9:         self.timestamp = datetime.datetime.now()', '10:         self.delivered = False', '11:         self.read = False', '12: ', '13:     def mark_as_delivered(self):', '14:         self.delivered = True', '15: ', '16:     def mark_as_read(self):', '17:         self.read = True'], 'chat.py': ['1: class Chat:', '2:     def __init__(self, id, participants):', '3:         self.id = id', '4:         self.participants = participants', '5:         self.messages = []', '6: ', '7:     def add_message(self, message):', '8:         pass', '9: ', '10:     def get_message(self, message_id):', '11:         pass', '12: ', '13:     def get_all_messages(self):', '14:         pass'], 'group_chat.py': ['1: from chat import Chat', '2: ', '3: class GroupChat(Chat):', '4:     def __init__(self, id, participants):', '5:         super().__init__(id, participants)', '6:         super().__init__(id, participants)', '7:         self.participants = list(participants)\n', '8:     def add_message(self, sender_id, content):', '9:         message = Message(len(self.messages), sender_id, self.id, content)', '10:         self.messages.append(message)', '11:         for participant in self.participants:', '12:             if participant.id != sender_id:', '13:                 participant.receive_message(self.id, message)\n', '14:     def get_message(self, message_id):', '15:         for message in self.messages:', '16:             if message.id == message_id:', '17:                 return message', '18:         return None\n', '19:     def get_all_messages(self):', '20:         return self.messages'], 'image_message.py': ['1: from message import Message', '2: ', '3: class ImageMessage(Message):', '4:     def __init__(self, id, sender, receiver, content, image_file):', '5:         super().__init__(id, sender, receiver, content)', '6:         self.image_file = image_file'], 'controller.py': ['1: class Controller:', '2:     def __init__(self):', '3:         self.users = []', '4:         self.chats = []', '5: ', '6:     def create_user(self):', '7:         pass', '8: ', '9:     def create_chat(self):', '10:         pass', '11: ', '12:     def send_message(self):', '13:         pass', '14: ', '15:     def read_message(self):', '16:         pass', '17: ', '18:     def get_status(self):', '19:         pass', '20: ', '21:     def send_image_message(self):', '22:         pass']}
        new_file_dict = implement_git_diff_on_file_dict(file_dict, files_and_contents)
        print('')


        
if __name__ == '__main__':
    # unittest.main()

    cls = TestDiffUpdater()
    cls.setUp()
    # cls.test_write_files_edge_case_missing_modifier_for_blank_lines()
    # cls.test_line_indentation_fix_redux()
    cls.test_over_writing_files()

