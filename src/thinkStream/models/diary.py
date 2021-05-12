from __future__ import annotations
from typing import ClassVar

from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column
from sqlalchemy.types import DateTime, Integer, String, Text
from sqlalchemy import ForeignKey

from models import Base


class Diary(Base):
    __tablename__ = 'diaries'
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    user_mail = Column(String(254))
    title = Column(String(200))
    thought_id = Column(Integer, ForeignKey('thoughts.id'))
    body = Column(Text)
    created = Column(DateTime)
    updated = Column(DateTime)
    thought = relationship("Thought", back_populates="diaries")
