from django.shortcuts import render
from django.http import HttpResponse

def navbar(request):
    return render(request,'navbar.html')

def projects(request):
    return render(request,'projects/projects.html')

def project(request):
    return render(request,'projects/single-project.html')
