from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse

def home(request):
     return render_to_response('home/home.html')
     
def publication(request):
    var = {}
    var['content'] = "not implemented"
    var['user'] = 'zq7m2E8AAAAJ'
    
    t = loader.get_template('main.html')
    c = Context(var)
    
    return HttpResponse(t.render(c))
    
    return render_to_response(request, 'main.html', var)
