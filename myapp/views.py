from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask
from .forms import CreateNewProject
# Create your views here.


def index(request):
    title = "django course!!"
    return render(request, "index.html", {
        'title': title
    })


def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" % username)


def about(request):
    return HttpResponse("<h1>About</h1>")


def projects(request):
    projects = Project.objects.all()
    return render(request, "projects/projects.html", {
        "projects": projects
    })


def tasks(request):
    # task= get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html", {
        "tasks": tasks
    })


def create_tasks(request):
    if request.method == "GET":
        return render(request, "tasks/create_task.html", {
            'form': CreateNewTask()})
    else:
        Task.objects.create(
            title=request.POST["title"], description=request.POST["description"], project_id=2)
        return redirect('tasks')


def create_project(request):
    if request.method == "GET":
        return render(request, "projects/create_project.html", {
            'form': CreateNewProject()})
    else:
        project= Project.objects.create(
            name=request.POST["name"]
        )
        return redirect('projects')

def project_detail(request, id):
    proyecto= get_object_or_404(Project, id=id)
    tasks=Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html',{
        'project':proyecto,
        'tasks': tasks
    })