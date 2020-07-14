from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'index.html', {})

def projects_view(request):
    return render(request, 'projects.html', {})

def resume_view(request):
    return render(request, 'resume.html', {})

def contact_view(request):
    return render(request, 'contact.html', {})

def about_view(request):
    return render(request, 'about.html', {})