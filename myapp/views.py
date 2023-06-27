from django.http import HttpResponse
from .models import Task, Project
from django.shortcuts import render, redirect
from .forms import CreateNewTask

# Create your views here.
def index(request):
    title = 'Welcome to Django!'
    return render(request, 'index.html', {'title': title})

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)

def about(request):
    username = 'jandr'
    return render(request, 'about.html', {'username': username})

def projects(request):
    projects = list(Project.objects.all())
    return render(request, 'projects.html', {'projects': projects})

def tasks(request):
    #task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {'form': CreateNewTask()})
    else:
        Task.objects.create(name=request.POST['name'], description=request.POST['description'], project_id=1)
        return redirect('/tasks/')