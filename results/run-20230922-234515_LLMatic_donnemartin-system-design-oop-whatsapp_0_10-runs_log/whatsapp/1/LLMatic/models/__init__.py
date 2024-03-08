from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .contact import Contact
from .user import User
