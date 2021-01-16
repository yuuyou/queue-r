from sqlalchemy import Column, String

from db import Base

class Verification(Base):
    __tablename__ = 'verifications'

    id = Column(String, primary_key=True)
    email = Column(String, unique=True)
    temp_pass = Column(String)