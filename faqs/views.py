from django.shortcuts import render
from .models import language,topic,question,subtopic

# Create your views here.
def faqview(request,name,pk=1,spk=1):
    languages = language.objects.all()
    topics = topic.objects.all()
    subtopics = subtopic.objects.all()
    questions = question.objects.all()

    return render(request,'faqs/faq.html',{'name':name,'languages':languages,'topics': topics,'subtopics':subtopics,'questions':questions,'pk':pk,'spk':spk})

