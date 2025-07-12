from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'schedule', 'is_active', 'status', 'last_run', 'created_at')
    list_filter = ('schedule', 'is_active', 'status')

admin.site.register(Task, TaskAdmin)
# Register your models here.
