import os
import server

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))