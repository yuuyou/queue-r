from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship
from db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String, nullable=True, unique=True)
    telephone = Column(String)

    store = relationship("Store", back_populates="owner", cascade="all, delete", passive_deletes=True)
    queue = relationship("Queue", back_populates="user", cascade="all, delete", passive_deletes=True)