from django.shortcuts import render_to_response

def home(request):
     return render_to_response('home/home.html')
     
def publication(request):
    var = {}
    var['content'] = "not implemented"
    var['user'] = 'zq7m2E8AAAAJ'
    return render_to_response(request, 'main.html', var)
