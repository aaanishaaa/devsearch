from django.urls import path
from . import views

urlpatterns = [
    path("tasks/", views.tasks, name='tasks'),
    path("tasks/<str:pk>/", views.task, name='task')
]