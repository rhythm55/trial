from django.shortcuts import render
from .models import language,topic,sstopic,subtopic

# Create your views here.
def material(request,name,pk=1,spk=1):
    languages = language.objects.all()
    topics = topic.objects.all()
    subtopics = subtopic.objects.all()
    sstopics = sstopic.objects.all()

    return render(request,'materials/home.html',{'name':name,'languages':languages,'topics': topics,'subtopics':subtopics,'sstopics':sstopics,'pk':pk,'spk':spk})

