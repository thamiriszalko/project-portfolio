from django.shortcuts import render, get_object_or_404
from .models import Blog


def home(request):
    posts = Blog.objects.all()

    return render(
        request,
        'blog/home.html',
        {'posts': posts},
    )


def post_detail(request, pk):
    post_detail = get_object_or_404(Blog, id=pk)

    return render(
        request,
        'blog/post_detail.html',
        {'post_detail': post_detail},
    )
