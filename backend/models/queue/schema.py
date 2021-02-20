from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class Queue(Base):
    __tablename__ = "queues"

    id = Column(String, primary_key=True)
    store_id = Column(String, ForeignKey('stores.id', ondelete='CASCADE'))
    user_id = Column(String, ForeignKey('users.id', ondelete='CASCADE'))
    queue_number = Column(Integer)
    number_of_people = Column(Integer)
    queue_status = Column(String)

    store = relationship("Store", back_populates="queues")
    user = relationship("User", back_populates="queue")