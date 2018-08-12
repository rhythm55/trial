from django.urls import path
from . import views

urlpatterns = [
    path('',views.faqview,name='faqview'),
    path('<int:pk>/',views.faqview,name='faqview'),
    path('<int:pk>/<int:spk>/',views.faqview,name='faqview'),
    ]