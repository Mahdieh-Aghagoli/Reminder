from django import forms
from rest_framework.exceptions import ValidationError

from apps.todo.models import Task, Category


class RegisterTaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', 'category', 'due_date', 'priority']


class RegisterCategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', ]

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if name == '':
            raise ValidationError('Name needed')
