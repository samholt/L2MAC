
# Import necessary libraries
import os
import socket

# Function to check connectivity
def check_connectivity():
    try:
        # connect to the host -- tells us if the host is actually reachable
        socket.create_connection(('Google.com', 80))
        return True
    except OSError:
        pass
    return False

# Function to handle offline mode
def handle_offline_mode():
    # If there is no connectivity, queue the messages for later
    if not check_connectivity():
        # TODO: Add code to queue messages
        pass