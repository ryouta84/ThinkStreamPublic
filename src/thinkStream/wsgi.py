from pyramid.paster import get_app
import os

ini_path = os.path.dirname(os.path.abspath(__file__)) + '/production.ini'

application = get_app(ini_path, 'main')
