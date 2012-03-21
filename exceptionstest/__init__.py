from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('hello_world','/hello_world')
    config.add_subscriber(\
        add_test_new_response,
        "pyramid.events.NewResponse")
    config.scan()
    return config.make_wsgi_app()

def add_test_new_response(event):
    if event.request.path_info == '/hello_world':
        print "=======================" 
        print "add_test_new_response"
        print "?? event.request exception?"
        if hasattr( event.request, 'exception' ):
            print "-- Yes"
            print event.request.exception
        else:
            print "-- No"
        print "-----------------------"



