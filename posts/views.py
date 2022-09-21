from django.shortcuts import render
from . models import Post
from django.views.generic import ListView

# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "posts/home.html", context)


class PostListView(ListView):
    model = Post
    template_name = "posts/home.html"
    context_object_name: "posts"

    #<app>/<model>_<view_type>.html

def about(request):
    return render(request, "posts/about.html", {'title':"About"})