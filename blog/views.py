from django.shortcuts import render
from .models import *


def index(request):
    posts = Blogpost.objects.all()

    context = {'posts':posts}
    return render(request,'blog/index.html',context)

def blogpost(request,id):

    post = Blogpost.objects.get(post_id=id)
    
    context = {'post':post}
    return render(request,'blog/blogpost.html',context)