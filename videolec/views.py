from django.shortcuts import render

def home(request):
    return render(request,'videolec/home.html')
