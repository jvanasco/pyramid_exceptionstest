from pyramid.view import view_config

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project':'ExceptionsTest'}

@view_config(route_name="hello_world", renderer="templates/hello_world.pt")
def hello_world(request):
    raise ValueError('Value Error')
    return {'project':'ExceptionsTest'}
