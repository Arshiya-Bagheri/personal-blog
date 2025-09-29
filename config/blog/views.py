from django.shortcuts import render
from .models import Blogs
from django.contrib.auth.decorators import user_passes_test
# USERNAME: arshiya
# PASS: 01arshiya01
def superuser_required(view_func):
    decorator = user_passes_test(lambda u: u.is_superuser)
    return decorator(view_func)

def base(request):
    return render(request, 'blog/base.html')

def blogs(request):
    blogs = Blogs.objects.all().order_by('created_at')
    return render(request, 'blog/blogs.html', {'blogs': blogs})

def search(request):
    title_query = request.GET.get('title', '')
    created_query = request.GET.get("created", "")
    updated_query = request.GET.get("updated", "")

    results = None  # default: nothing shown

    # Run filters only if user provided at least one search term
    if title_query or created_query or updated_query:
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

@superuser_required
def add_blog(request):
    return render(request, 'blog/add_blog.html')

@superuser_required
def update_blogs(request):
    return render(request, 'blog/update_blogs.html')