from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField(blank=True)
    schedule = models.CharField(max_length=50)  # e.g., "daily", "weekly"
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=50)
    last_run = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name