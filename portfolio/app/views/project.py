from django.views.generic import ListView, DetailView
from ..models import Project

class ProjectListView(ListView):
    model = Project
    template_name = 'app/project_list.html'
    context_object_name = 'projects'
    ordering = ['-created_at']  # Show newest projects first

    def get_queryset(self):
        return super().get_queryset().order_by('-created_at')

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'app/project_detail.html'
    context_object_name = 'project' 