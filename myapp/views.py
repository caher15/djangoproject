from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from .models import Project, Task 

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

def projects(request):
    projects = list(Project.objects.values())# instancia se convierte en lista de python
    return JsonResponse(projects, safe=False) #objeto y se pasa de safe a false

def tasks(request, id):
    #tasks = Task.objects.get(id=id)
    tasks = get_object_or_404(Task, id=id)
    return HttpResponse('Task: %s' % tasks.title)

    