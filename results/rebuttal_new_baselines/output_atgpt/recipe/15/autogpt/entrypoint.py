import os
import server

# Initialize the server
server = server.Server()

# Set up the server
if __name__ == '__main__':
    server.run(host='0.0.0.0', port=os.getenv('PORT', 5000))