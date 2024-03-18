# Group Chat Module

class GroupChat:
    def __init__(self, group_name, group_picture):
        self.group_name = group_name
        self.group_picture = group_picture
        self.participants = {}
        self.admins = {}

    # Group Creation
    def create_group(self, group_details):
        # Validate the group details
        if not validate_group_details(group_details):
            return 'Invalid group details'
        # Store the group details
        self.group_details = group_details
        return 'Group created successfully'

    # Participant Management
    def add_participant(self, participant_id):
        # Validate the participant details
        if not validate_participant_details(participant_id):
            return 'Invalid participant details'
        # Store the participant details
        self.participants[participant_id] = 'member'
        return 'Participant added successfully'

    def remove_participant(self, participant_id):
        # Remove the participant details
        del self.participants[participant_id]
        return 'Participant removed successfully'

    # Admin Roles and Permissions
    def assign_admin(self, participant_id):
        # Validate the participant details
        if not validate_participant_details(participant_id):
            return 'Invalid participant details'
        # Store the admin roles and permissions
        self.admins[participant_id] = 'admin'
        return 'Admin role assigned successfully'