from django.shortcuts import render
from .models import project,steps
def view_projects(request):
    projects = project.objects.all
    return render(request,'projects/project_view.html',{'projects':projects})

def project_steps(request,projectid=1,stepno=1):
    projects = project.objects.all
    stepss = steps.objects.all
    return render(request,'projects/project_steps.html',{'projectid':projectid,'steps':stepss,'projects':projects,'stepno':stepno})
