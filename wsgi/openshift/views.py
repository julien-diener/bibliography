from django.shortcuts import redirect
from django.template import Context, loader
from django.http import HttpResponse

import gcitation

def home(request):
    return redirect('publication')
     
def publication(request):
    var = {}
    var['user'] = 'zq7m2E8AAAAJ'
    
    
    query = gcitation.Query(var['user'])
    
    if query.error:
        return HttpResponse(query.html)
    
    var['username'] = query.username
    var['publication'] = query.publication
    #var['content'] = "not implemented\n\n" + repr(query)
    
    
    t = loader.get_template('main.html')
    c = Context(var)
    
    return HttpResponse(t.render(c))

