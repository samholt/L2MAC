import os
import server

if __name__ == '__main__':
    server.setup()
    server.run(os.getenv('PORT', 8000))