from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from . import Base


class Contact(Base):
	__tablename__ = 'contacts'

	id = Column(Integer, primary_key=True, index=True)
	user_id = Column(Integer, ForeignKey('users.id'))
	contact_id = Column(Integer, ForeignKey('users.id'))
	blocked = Column(Boolean, default=False)

	user = relationship('User', foreign_keys=[user_id])
	contact = relationship('User', foreign_keys=[contact_id])
