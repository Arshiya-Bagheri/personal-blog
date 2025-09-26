from django.shortcuts import render

def base(request):
    return render(request, 'blog/base.html')

def blogs(request):
    return render(request, 'blog/blogs.html')

def search(request):
    return render(request, 'blog/search.html')

def about(request):
    return render(request, 'blog/about.html')