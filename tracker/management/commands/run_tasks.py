from django.core.management.base import BaseCommand
from tracker.models import Task
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Simulates running all active tasks'

    def handle(self, *args, **kwargs):
        tasks = Task.objects.filter(is_active=True)
        for task in tasks:
            task.status = random.choice(['success', 'failed'])  # simulate result
            task.last_run = timezone.now()
            task.save()
            self.stdout.write(self.style.SUCCESS(f"{task.name} → {task.status}"))
