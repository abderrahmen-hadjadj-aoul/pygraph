from django.shortcuts import render
from .models import Workspace

# HOME

def home(request):
    context = {
        'message': 'Hello',
    }
    return render(request, 'graphs/home.html', context)

# WORKSPACE

def workspace_index(request):
    context = {
        'message': 'Hello',
        'workspaces': Workspace.objects.all(),
    }
    return render(request, 'graphs/workspace.html', context)

def workspace_create(request):
    if request.POST:
        name = request.POST['name']
        description = request.POST['description']
        workspace = Workspace.objects.create(name=name, description=description)
        workspace.save()
    return render(request, 'graphs/workspace.create.html')
