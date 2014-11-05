from django.shortcuts import render

from projects.models import Project


def home(request):
    projects = Project.objects.all()

    data = {
        'projects': projects
    }
    return render(request, 'main/index.html', data)
