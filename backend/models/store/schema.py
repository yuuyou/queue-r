from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Store(Base):
    __tablename__ = "stores"

    id = Column(String, primary_key=True)
    owner_id = Column(String, ForeignKey('users.id', ondelete='CASCADE'))
    name = Column(String)

    owner = relationship("User", back_populates="store")
    queues = relationship("Queue", back_populates="store", cascade="all, delete", passive_deletes=True)