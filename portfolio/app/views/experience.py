from django.views.generic import ListView, DetailView
from ..models import Experience

class ExperienceListView(ListView):
    model = Experience
    template_name = 'app/experience_list.html'
    context_object_name = 'experiences'
    ordering = ['-start_date']  # Show most recent experiences first

    def get_queryset(self):
        return super().get_queryset().order_by('-start_date', '-end_date')

class ExperienceDetailView(DetailView):
    model = Experience
    template_name = 'app/experience_detail.html'
    context_object_name = 'experience' 