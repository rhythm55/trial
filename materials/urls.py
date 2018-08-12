from django.urls import path
from . import views

urlpatterns = [
    path('',views.material,name='material'),
    path('(?<pk>\d+)/',views.material,name='material'),
    path('(?<pk>\d+)/(?<spk>\d+)/',views.material,name='material'),
    ]