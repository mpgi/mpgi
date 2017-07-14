from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import CreateProjectForm
from .models import Project

# Create your views here.
def editor(request):
    return render(request, 'editor/editor.html', {})

def create_project(request):
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.create_time = timezone.now()
            project.last_modified_date = timezone.now()
            project.save()
            return redirect('editor')
    else:
        form = CreateProjectForm()
    return render(request, 'editor/create_project.html', {'form': form})

def load_project(request):
    projects = Project.objects.order_by('last_modified_date') 
    return render(request, 'editor/load_project.html', {'projects': projects})
