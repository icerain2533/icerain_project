from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config, notfound_view_config
from phoneweb.com.util import ETXMLManager


@view_config(route_name='home', renderer='templates/index.html')
def read(request):
    return {
        "userInfos":ETXMLManager.read_xml()
    }

@view_config(route_name='delete', renderer='json')
def delete(request):
    id = request.GET.get("id")
    return {
        "result":  ETXMLManager.delete(id)
    }


def insertM(request):
    name = request.GET.get("name")
    telephone = request.GET.get("telephone")
    return {
        "result":  ETXMLManager.insert(name, telephone)
    }

@view_config(route_name='toEdit', renderer='templates/contact/editUser.html')
def toEdit(request):
    return {
        "id":request.GET.get("id"),
        "name":request.GET.get("name"),
        "telephone":request.GET.get("telephone")
    }

@view_config(route_name='edit', renderer='json')
def edit(request):
     id = request.GET.get("id")
     name =  request.GET.get("name")
     tele =  request.GET.get("telephone")
     return {
         "result": ETXMLManager.update(id, name,tele)
     }

@view_config(route_name='toCreate',renderer='templates/contact/createUser.html')
def toCreate(request):
     return {}

@view_config(route_name='create', renderer='json')
def createUser(request):
     name =  request.GET.get("name")
     tele =  request.GET.get("telephone")
     return {
         "result": ETXMLManager.insert(name,tele)
     }

