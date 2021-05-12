from __future__ import annotations
from typing import ClassVar

from sqlalchemy.schema import Column
from sqlalchemy.types import DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import Table, ForeignKey

from models import Base


class Thought(Base):
    __tablename__ = 'thoughts'
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    user_mail = Column(String(254))
    thought = Column(String(100))
    diaries = relationship('Diary', back_populates='thought')
