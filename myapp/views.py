from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from .models import Project, Task 
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = "Django Course!!"
    username = "juan"
    return render(request, 'index.html', {
        'title' : title,
        'username' : username
    })

def hello(request, username):
    return HttpResponse("<h1>Hello World! %s </h1>" % username)

def send(request, id):
    print(type(id))
    return HttpResponse("<h1>Hello World! %s </h1>" % id)

def about(request):
    return render(request, 'about.html')

def projects(request):
    #projects = list(Project.objects.values())# instancia se convierte en lista de python
    projects = Project.objects.all()
    return render(request , 'projects/projects.html', {
        'projects' : projects
    })
    #return JsonResponse(projects, safe=False) #objeto y se pasa de safe a false

def tasks(request):
    #tasks = Task.objects.get(id=id)
    #tasks = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks' : tasks
        })
    #return HttpResponse('Task: %s' % tasks.title)

def create_task(request):
    # print(request.GET['title'])
    # print(request.GET['description'])
    # create using the foreign key id field to hardcode project with id=2
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html',{
            'form' : CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')
    
def create_projects(request):
    if request.method == 'GET':
        return render(request,'projects/create_projects.html', {
            'form' : CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect('projects')