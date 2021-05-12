from datetime import datetime, date
from typing import Dict, Any

from pyramid.request import Request
from pyramid.view import view_config

from models import DBSession
from models.diary import Diary
from models.user import RootFactory


class DiariesList():
    def __init__(self, request: Request) -> None:
        self.request = request

    @view_config(route_name="diaries_list", renderer="templates/diaries_list.jinja2", permission=RootFactory.PERMISSION_EDIT)
    def index(self) -> Dict[Any, Any]:
        diaries_list = DBSession.query(Diary).filter(
            Diary.user_mail == self.request.authenticated_userid).order_by(Diary.created).all()
        thought_list = [(diary.thought.thought, []) for diary in diaries_list]
        result = dict(thought_list)
        for diary in diaries_list:
            result[diary.thought.thought].append(diary)
        return dict(time=datetime.now(), logged_in=self.request.authenticated_userid, diaries_list=result)
