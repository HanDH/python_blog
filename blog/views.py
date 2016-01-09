from django.http.response import HttpResponse
from blog.models import Post
from django.views.generic import ListView, DetailView



class PostList(ListView):
    model = Post
    template_name = 'home.html'



class PostDetail(DetailView):
    model = Post
    template_name = 'detail.html'
