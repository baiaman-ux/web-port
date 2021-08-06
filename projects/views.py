from django.shortcuts import render

from projects.models import Project
from django.views.generic import ListView, DetailView



class ProjectView(ListView):
    model = Project
    template_name = 'projects/project_index.html'
    context_object_name = 'projects'

class DetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'