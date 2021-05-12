from __future__ import annotations
from typing import Dict, Any

from pyramid.view import view_config, forbidden_view_config
from pyramid.security import (remember, forget)
from pyramid.httpexceptions import HTTPSeeOther
from pyramid.request import Request

from models import DBSession
from models.user import User, RootFactory
from helper.util import clear_msg, flash_msg


class Home():
    def __init__(self, request: Request) -> None:
        self.request = request

    @view_config(route_name="home", renderer="templates/home.jinja2", permission=RootFactory.PERMISSION_VIEW)
    def index(self) -> Dict[Any, Any]:
        return dict()

    @view_config(route_name='create_user', renderer='templates/login.jinja2', permission=RootFactory.PERMISSION_VIEW)
    def create_user(self):
        clear_msg(self.request)

        mail = self.request.params.get('mail')
        name = self.request.params.get('name')
        password = self.request.params.get('password')
        if not (mail and name and password):
            return HTTPSeeOther(location='/')

        user = None
        try:
            user = User.create(mail, name, password)
        except Exception as e:
            flash_msg(self.request, 'Failed to register.')
            return HTTPSeeOther(location='/create_user')

        if user is not None:
            message = "Success create user."

        return dict(message=message)

    @view_config(route_name='login', renderer='templates/login.jinja2', permission=RootFactory.PERMISSION_VIEW)
    @forbidden_view_config(renderer='templates/login.jinja2')
    def login(self):
        message = ''

        if 'submitted' in self.request.params:
            mail = self.request.params.get('mail')
            password = self.request.params.get('password')
            user = None
            try:
                user = DBSession.query(User).filter(User.mail == mail).one()
                if user.login(password):
                    headers = remember(self.request, mail)
                    return HTTPSeeOther(location='/diaries_list', headers=headers)
                message = 'Password does not match.'
            except Exception as e:
                message = 'User does not exist.'

        return dict(message=message)
