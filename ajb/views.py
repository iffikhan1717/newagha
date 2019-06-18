from django.shortcuts import render
from .models import Post

def home(request):
    psts = Post.objects.all()
    return  render(request,'master/index.html', context={'object_list':psts})


# def allpst(request):
#     psts = Post.objects.all()
#
#     return render(request,'pros/blog.html', context={'object_list':psts})

