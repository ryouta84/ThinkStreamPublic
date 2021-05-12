import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from zope.sqlalchemy import register


Base = declarative_base()
dialect = 'mysql'
driver = 'pymysql'
host = 'think_stream_db'
port = 3306
user = os.environ['MYSQL_APP_USER']
password = os.environ['MYSQL_APP_PASSWORD']
db = 'thinkStream_user'
charset = 'utf8'
engine = create_engine(
    f"{dialect}+{driver}://{user}:{password}@{host}:{port}/{db}?charset={charset}")

DBSession = scoped_session(sessionmaker(bind=engine))
register(DBSession)
Base.metadata.bind = engine
