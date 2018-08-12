from django.urls import path
from . import views

urlpatterns = [
    path('',views.blogall,name='blogall'),
    path('<int:blogid>',views.blogview,name='blogview'),
]