from django.contrib import admin
from .models import Experience, Skill, Project

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date')
    search_fields = ('title', 'company', 'description')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'github_link', 'live_demo', 'created_at')
    search_fields = ('title', 'description')
