import pickle


class DataStore:
    def __init__(self, filename):
        self.filename = filename

    def save_data(self, data):
        with open(self.filename, 'wb') as file:
            pickle.dump(data, file)

    def load_data(self):
        try:
            with open(self.filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return None


data_store = DataStore('gcs_data.pkl')


def save_state(user_manager, user_profile_manager, contact_manager, message_manager, group_chat_manager, status_story_manager):
    data = {
        'user_manager': user_manager,
        'user_profile_manager': user_profile_manager,
        'contact_manager': contact_manager,
        'message_manager': message_manager,
        'group_chat_manager': group_chat_manager,
        'status_story_manager': status_story_manager
    }
    data_store.save_data(data)


def load_state():
    data = data_store.load_data()
    if data:
        return data['user_manager'], data['user_profile_manager'], data['contact_manager'], data['message_manager'], data['group_chat_manager'], data['status_story_manager']
    return None