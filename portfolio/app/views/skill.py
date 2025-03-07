from django.views.generic import ListView
from ..models import Skill

class SkillListView(ListView):
    model = Skill
    template_name = 'app/skill_list.html'
    context_object_name = 'skills'
    ordering = ['-level']  # Show highest level skills first

    def get_queryset(self):
        return super().get_queryset().order_by('-level', 'name') 