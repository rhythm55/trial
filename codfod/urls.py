"""codfod URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views as view_home
from django.conf import settings
from materials import views as view_material
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view_home.home,name='home'),
    path('projects/',include('projects.urls')),
    path('blogs/',include('blogs.urls')),
    path('faqs/<slug:name>/',include('faqs.urls')),
    path('interview/',include('interview.urls')),
    path('materials/(?P<name>(\s+)/',include('materials.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




