from django.urls import path
from . import views

urlpatterns = [
    path("", views.projects, name='projects'),
    path("project/<int:id>/", views.project, name='project'),
    path('create-project/',views.createProject, name='create-project')
]