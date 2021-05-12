from typing import Any
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.session import SignedCookieSessionFactory
from pyramid.config import Configurator

from helper.security import groupfinder

def main(global_config: Any, **settings: Any) -> Configurator:
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(
        settings=settings, root_factory='models.user.RootFactory')

    # クッキーに認証トークンを持たせるのでサーバーが複数あってもセッションレプリケーションが不要な認証
    authn_policy = AuthTktAuthenticationPolicy(
        os.environ['AUTHTKT_SECRET'], callback=groupfinder, hashalg='sha512', max_age=60 * 60 * 24, timeout=60 * 60, reissue_time=60 * 2)
    authz_policy = ACLAuthorizationPolicy()
    my_session_factory = SignedCookieSessionFactory(os.environ['SIGNED_COOKIE_SESSION_SECRET'])

    config.set_session_factory(my_session_factory)
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.include('.routes')
    # viewsを最初にscanしないと以下のようなエラーが出る
    # sqlalchemy.exc.InvalidRequestError: Multiple classes found for path "models.diary.Diary" in the registry of this declarative base. Please use a fully module-qualified path.
    config.scan(".views")
    return config.make_wsgi_app()
