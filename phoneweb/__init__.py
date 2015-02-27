import pkg_resources
from pyramid.config import Configurator
import os
from pyramid.httpexceptions import HTTPNotFound
from views import insertM


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    config = Configurator(settings=settings)
    config.include('pyramid_mako')
    config.add_mako_renderer('.html')
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home','/')
    config.add_route('insert','/insert')
    config.add_route('delete','/delete')
    config.add_route('toEdit','/toEdit')
    config.add_route('edit','/edit')
    config.add_route('toCreate','/toCreate')
    config.add_route('create','/create')
    config.add_view(insertM,route_name="insert")
    config.scan("phoneweb")


    return config.make_wsgi_app()