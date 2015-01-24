from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    keys = Column(String(50), unique=False)

    def __init__(self):
        self.keys = ''

    def add_key(self, key):
        self.keys = self.keys + key
        return self.keys
