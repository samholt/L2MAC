from flask import Flask, request
from dataclasses import dataclass

app = Flask(__name__)

# In-memory database
DB = {
    'users': [],
    'clubs': [],
    'books': [],
    'meetings': [],
    'discussions': [],
    'resources': []
}

@dataclass
class User:
    id: int
    name: str
    email: str
    read_list: list
    clubs: list

@dataclass
class Club:
    id: int
    name: str
    description: str
    is_private: bool
    members: list
    books: list

@dataclass
class Book:
    id: int
    title: str
    author: str

@dataclass
class Meeting:
    id: int
    club_id: int
    book_id: int
    date: str

@dataclass
class Discussion:
    id: int
    club_id: int
    book_id: int
    user_id: int
    comment: str

@dataclass
class Resource:
    id: int
    title: str
    link: str

@app.route('/users', methods=['POST'])
def create_user():
    user = User(**request.json)
    DB['users'].append(user)
    return {'id': user.id}, 201

@app.route('/clubs', methods=['POST'])
def create_club():
    club = Club(**request.json)
    DB['clubs'].append(club)
    return {'id': club.id}, 201

@app.route('/books', methods=['POST'])
def create_book():
    book = Book(**request.json)
    DB['books'].append(book)
    return {'id': book.id}, 201

@app.route('/meetings', methods=['POST'])
def create_meeting():
    meeting = Meeting(**request.json)
    DB['meetings'].append(meeting)
    return {'id': meeting.id}, 201

@app.route('/discussions', methods=['POST'])
def create_discussion():
    discussion = Discussion(**request.json)
    DB['discussions'].append(discussion)
    return {'id': discussion.id}, 201

@app.route('/resources', methods=['POST'])
def create_resource():
    resource = Resource(**request.json)
    DB['resources'].append(resource)
    return {'id': resource.id}, 201

if __name__ == '__main__':
    app.run(debug=True)
