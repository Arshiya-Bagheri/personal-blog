from django.shortcuts import render
from .models import Blogs

def base(request):
    return render(request, 'blog/base.html')

def blogs(request):
    blogs = Blogs.objects.all().order_by('created_at')
    return render(request, 'blog/blogs.html', {'blogs': blogs})

def search(request):
    title_query = request.GET.get('title', '')
    created_query = request.GET.get("created", "")
    updated_query = request.GET.get("updated", "")

    results = Blogs.objects.all()
    
    if title_query:
        results = results.filter(title__icontains=title_query)
    if created_query:
        results = results.filter(created_at__date=created_query)
    if updated_query:
        results = results.filter(updated_at__date=updated_query)

    return render(request, 'blog/search.html', {'results': results})

def about(request):
    return render(request, 'blog/about.html')