from __future__ import annotations
from typing import Union, List, Any
import time

from pyramid.security import (
    Allow,
    Everyone,
    )

from models import Base, DBSession
import helper.security

from sqlalchemy.schema import Column
from sqlalchemy.types import DateTime, Integer, String

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {"extend_existing": True}

    id =       Column(Integer, primary_key=True)
    mail =     Column(String(254))
    username = Column(String(40))
    password = Column(String(60))
    groups =   Column(String(50))
    created =  Column(DateTime)

    GROUP_ADMIN = 'admin'
    GROUP_GENERAL = 'general'

    @classmethod
    def create(cls, mail: str, name: str, password: str, groups: Union[str, None] = None) -> User:
        """
        usersテーブルにレコードを作成する。
        """
        now = time.strftime('%Y-%m-%d %H:%M:%S')

        hashed_password = helper.security.hash_password(password)
        if groups is None:
            groups = cls.GROUP_GENERAL

        new_user = User()
        new_user.mail = mail
        new_user.username = name
        new_user.password = hashed_password
        new_user.groups = groups
        new_user.created = now
        try:
            DBSession.add(new_user)
        except Exception as e:
            DBSession.rollback()
            raise e

        return new_user

    def login(self, password: str) -> bool:
        return helper.security.check_password(password, self.password)

    def get_groups(self) -> List[str]:
        return self.groups.split(',')

class RootFactory():
    PERMISSION_VIEW = 'view'
    PERMISSION_EDIT = 'edit'

    __acl__ = [
        (Allow, Everyone, PERMISSION_VIEW),
        (Allow, User.GROUP_GENERAL, PERMISSION_EDIT)
    ]

    def __init__(self, request: Any) -> None:
        pass
