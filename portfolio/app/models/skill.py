from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(
        validators=[
            MinValueValidator(0, "Skill level cannot be less than 0"),
            MaxValueValidator(100, "Skill level cannot be more than 100")
        ]
    )

    class Meta:
        ordering = ['-level']  # Highest level first

    def __str__(self):
        return self.name 