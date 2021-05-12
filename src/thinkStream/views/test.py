from pyramid.view import view_config

@view_config(route_name="test", renderer='templates/mytemplate.jinja2')
def index(request):
    return {'project':'thinkStream in docker!!'}