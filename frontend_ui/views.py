from django.shortcuts import render, redirect
from django.db.models import Q
from django.conf import settings
from resource_api.models import Resource

def home(request):
    search_query = request.GET.get('search', '')
    
    if search_query:
        links = Resource.objects.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    else:
        links = Resource.objects.all()
    
    categories = Resource.objects.values_list('category', flat=True).distinct()
    
    context = {
        'owner': settings.SITE_CONFIG['OWNER'],
        'categories': categories,
        'links': links,
        'search_query': search_query,
    }
    return render(request, 'home.html', context)

def add_resource(request):
    if request.method == 'POST':
        try:
            Resource.objects.create(
                title=request.POST['title'],
                description=request.POST['description'],
                url=request.POST['url'],
                category=request.POST['category']
            )
            return redirect('frontend_ui:home')
        except Exception as e:
            return render(request, 'add_resource.html', {
                'error': str(e)
            })
    
    categories = Resource.objects.values_list('category', flat=True).distinct()
    return render(request, 'add_resource.html', {
        'categories': categories
    })