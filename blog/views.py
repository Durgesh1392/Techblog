from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        'author':'durgesh kumar',
        'title': 'first blog',
        'content': 'first post content',
        'date_posted':' 27 aug, 2017'
    },
    {
        'author':'jitendra kumar',
        'title':'second blog',
        'content':'second post content',
        'date_posted':'12 jan, 2021'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', { 'title':'about'})
