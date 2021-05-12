import time
from datetime import datetime, date

from pyramid.httpexceptions import HTTPSeeOther
from pyramid.view import view_config

from models import DBSession
from models.diary import Diary
from models.thought import Thought
from models.user import RootFactory
from helper.util import delete_whitespace, flash_msg


class Editor():
    def __init__(self, request):
        self.request = request

    @view_config(route_name="edit", renderer="templates/editor.jinja2", permission=RootFactory.PERMISSION_EDIT)
    def edit(self):
        id = self.request.GET.get('id')
        user_id = self.request.authenticated_userid
        diary = None
        if user_id and id:
            diary = DBSession.query(Diary).\
                filter(Diary.user_mail == user_id, Diary.id == id).\
                one()

        return dict(time=datetime.now(), logged_in=user_id, id=id, diary=diary)

    @view_config(route_name="create_diary", renderer="templates/update.jinja2", permission=RootFactory.PERMISSION_EDIT)
    def create_diary(self):
        now: str = time.strftime('%Y-%m-%d %H:%M:%S')
        diary: Diary = Diary()
        diary.user_mail = self.request.authenticated_userid
        diary.title = self.request.params.get('title')
        diary.body = self.request.params.get('input_markdown')
        diary.created = now
        diary.updated = now

        param_thought = None if delete_whitespace(self.request.params.get('thought')) == '' else self.request.params.get('thought')
        if param_thought is None:
            # thoughtを入力していない場合は受け付けない
            flash_msg(self.request, 'invalid input')
            return HTTPSeeOther(location='/edit')

        thought: Thought = DBSession.query(Thought).filter(Thought.user_mail == self.request.authenticated_userid, Thought.thought == param_thought).all()
        if (thought):
            diary.thought = thought[0]
        else:
            diary.thought = Thought(
                user_mail=self.request.authenticated_userid, thought=param_thought)
        DBSession.add(diary)

        return dict(diary=diary)

    @view_config(route_name="update", renderer="templates/update.jinja2", permission=RootFactory.PERMISSION_EDIT)
    def update(self):
        user_id = self.request.authenticated_userid
        if user_id:
            if 'update' in self.request.params:
                diary_id = self.request.params.get('id')
                diary: Diary = DBSession.query(Diary).\
                    filter(Diary.user_mail == user_id, Diary.id == diary_id).\
                    one()
                diary.title = self.request.params.get('title')
                diary.body = self.request.params.get('input_markdown')
                diary.updated = time.strftime('%Y-%m-%d %H:%M:%S')

        return dict(diary=diary)
