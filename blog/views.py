from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.

# def Home(request):
#     context = {
#         'post': Post.objects.all()
#     }
#     return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'post'
    

class PostDetailView(DetailView):
    model = Post
    


def about(request):
    return render(request,'blog/about.html')