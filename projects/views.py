from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ProjectForm
from .models import Project

def navbar(request):
    return render(request,'navbar.html')

def projects(request):
    return render(request,'projects/projects.html')

def project(request):
    return render(request,'projects/single-project.html')

def createProject(request):
    form = ProjectForm()
    if request.method=='POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context={'form':form}
    return render(request,"projects/projects_form.html",context)
