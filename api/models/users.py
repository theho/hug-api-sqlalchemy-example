from sqlalchemy import Column, Integer, String

from ._base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), required=True)
