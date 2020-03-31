from django.shortcuts import render,get_object_or_404


from django.http import HttpResponse

from .models import project

# Create your views here.

def index(request):
    projects = projects.objects
    return render (request, 'projects/index.html',{'projects':projects})

def detail(request,project_id):
    project_detail = get_object_or_404(projects,pk=project_id)
    return render(request, 'projects/detail.html', {'projects':project_detail})
