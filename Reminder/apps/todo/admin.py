from django.contrib import admin

from .models.category import Category
from .models.task import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'priority', 'due_date']
    list_display_links = ['title', 'due_date', ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name', ]
