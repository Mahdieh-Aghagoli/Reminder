from django.db import models
from django.db.models.functions import Now


class PassedTasks(models.Manager):

    def get_passed_tasks(self):
        qs = super().get_queryset().filter(due_date__lt=Now())
        return qs


class EmptyCategories(models.Manager):
    def get_empty_categories(self):
        return [cat for cat in self.all() if not cat.task_set.all()]
