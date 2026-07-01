from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Index Page")

def hello(request, username):
    return HttpResponse("<h1>Hello World! %s </h1>" % username)

def send(request, id):
    print(type(id))
    return HttpResponse("<h1>Hello World! %s </h1>" % id)

def about(request):
    return HttpResponse('About')


    