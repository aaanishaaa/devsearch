from django.shortcuts import render
from django.http import HttpResponse

def tasks(request):
    return HttpResponse('hello')

def task(request,pk):
    return HttpResponse('hello your task is'+ ' '+ pk)
