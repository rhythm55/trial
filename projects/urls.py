from django.urls import path
from . import views



urlpatterns = [
    path('',views.view_projects,name='view_projects'),
    path('<int:projectid>/',views.project_steps,name='project_steps'),
    path('<int:projectid>/<int:stepno>',views.project_steps,name='project_steps'),
]