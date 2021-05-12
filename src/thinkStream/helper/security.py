from typing import List
import bcrypt

from pyramid.request import Request

from models import DBSession
from models.user import User


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt(rounds=10, prefix=b'2a')
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def check_password(password: str, expected_hash: str) -> bool:
    if expected_hash is not None:
        return bcrypt.checkpw(password.encode('utf-8'), expected_hash.encode('utf-8'))
    return False


def groupfinder(mail: str, request: Request) -> List[str]:
    """
    pyramidの認可処理で用意しないといけない関数です。
    ユーザーの所属するグループのリストを返す。
    
    Returns
    -------
    groups : string[]
        ユーザーのグループ
    """

    try:
        request_user = DBSession.query(User).filter(User.mail == mail).one()
        return request_user.get_groups()
    except Exception as e:
        return []
