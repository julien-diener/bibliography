from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse

import gcitation

def home(request):
     return render_to_response('home/home.html')
     
def publication(request):
    var = {}
    var['user'] = 'zq7m2E8AAAAJ'
    
    
    query = gcitation.Query(var['user'])
    var['title'] = query.title
    var['publication'] = query.publication
    #var['content'] = "not implemented\n\n" + repr(query)
    
    
    t = loader.get_template('main.html')
    c = Context(var)
    
    return HttpResponse(t.render(c))
    
    return render_to_response(request, 'main.html', var)
