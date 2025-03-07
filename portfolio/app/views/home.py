from django.views.generic import TemplateView
from ..models import Experience, Skill, Project

class HomeView(TemplateView):
    template_name = 'app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get latest experiences first
        context['experiences'] = Experience.objects.all().order_by('-start_date')[:3]
        # Get skills ordered by level
        context['skills'] = Skill.objects.all().order_by('-level')
        # Get latest projects first
        context['projects'] = Project.objects.all().order_by('-created_at')[:4]
        return context 