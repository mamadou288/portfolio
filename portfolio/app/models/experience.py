from django.db import models

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    class Meta:
        ordering = ['-start_date']  # Most recent first

    def __str__(self):
        return f"{self.title} at {self.company}" 