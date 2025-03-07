from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    github_link = models.URLField(null=True, blank=True)
    live_demo = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # Most recent first

    def __str__(self):
        return self.title 