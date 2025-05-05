from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'request/index.html')

def home(request):
    return render(request, 'request/index.html')

# /request/{algo}

def req(request):
    return render(request, 'request/index.html')

def app_attributes(request):
    return render(request, 'request/index.html')

def middleware(request):
    return render(request, 'request/index.html')

def querydict(request):
    return render(request, 'request/index.html')

def is_secure(request):
    return render(request, 'request/index.html')

# /response/{algo}

def res(request):
    return render(request, 'request/index.html')

def subclasses(request):
    return render(request, 'request/index.html')

def json(request):
    return render(request, 'request/index.html')

def streaming(request):
    return render(request, 'request/index.html')

def file(request):
    return render(request, 'request/index.html')

def base(request):
    return render(request, 'request/index.html')