from django.db import models
from django.template.defaultfilters import slugify

from apps.todo.manager import EmptyCategories


class Category(models.Model):
    name = models.CharField('Category Name', max_length=100, unique=True)
    slug = models.SlugField(verbose_name='Slug')
    objects = EmptyCategories()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
