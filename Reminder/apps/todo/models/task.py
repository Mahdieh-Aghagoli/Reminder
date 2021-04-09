from django.db import models
from django.db.models import SET_NULL
from django.template.defaultfilters import slugify
from django.urls import reverse, NoReverseMatch
from django.utils.timezone import now

from apps.todo.manager import PassedTasks
from apps.todo.models import Category


class Task(models.Model):
    title = models.CharField('Title', max_length=100)
    content = models.TextField('Content', blank=True)
    created = models.DateTimeField(default=now)
    due_date = models.DateTimeField('Due Date', default=now)
    PRIORITY_CHOICES = [('Urgent', 'Urgent'),
                        ('High', 'High'),
                        ('Medium', 'Medium'),
                        ('Low', 'Low')]
    priority = models.CharField('Priority', max_length=6, choices=PRIORITY_CHOICES, default='Medium')
    category = models.ForeignKey(Category, on_delete=SET_NULL, blank=True, null=True, default='')

    objects = PassedTasks()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        try:
            return reverse('task_detail', args=(str(self.id)))
        except NoReverseMatch:
            return reverse('404')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
