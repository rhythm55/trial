from django.shortcuts import render
from . models import blog

def blogall(request):
    blogs = blog.objects.all().order_by('-pub_date')
    return render(request,'blogs/blogall.html',{'blogs':blogs})

new =[]

def blogview(request,blogid):
    blogs = blog.objects.all().order_by('-pub_date')
    return render(request,'blogs/blogview.html',{'blogs':blogs,'blogid':blogid,'new':new})
