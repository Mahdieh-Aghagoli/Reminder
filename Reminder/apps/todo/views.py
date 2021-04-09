from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.base import View
from rest_framework.generics import get_object_or_404

from apps.todo.forms import RegisterTaskModelForm, RegisterCategoryModelForm
from apps.todo.models import Task, Category


class TaskList(ListView):
    model = Task
    context_object_name = 'Task_List'


class OrderedTaskList(ListView):
    model = Task
    template_name = "todo/o_task_list.html"
    context_object_name = 'Tasks_List'
    queryset = Task.objects.order_by('-due_date')


class TaskDetail(DetailView):
    model = Task
    template_name = 'todo/task_detail.html'


class CategoryList(ListView):
    model = Category
    context_object_name = 'Cat_List'


class CategoryTaskList(ListView):
    template_name = 'todo/category_task.html'

    def get_queryset(self):
        self.title = get_object_or_404(Task, pk=self.kwargs['pk'])
        return Task.objects.filter(category__task__title__in=[self.title]).order_by('-due_date')


class AddTask(View):
    def get(self, request):
        form = RegisterTaskModelForm()
        return render(request, 'todo/add_task.html', {'form': form})

    def post(self, request):
        form = RegisterTaskModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            task = Task(**data)
            task.save()
            return redirect('ok')
        return render(request, 'todo/add_task.html', {'form': form})


class AddCategory(View):
    def get(self, request):
        form = RegisterCategoryModelForm()
        return render(request, 'todo/add_category.html', {'form': form})

    def post(self, request):
        form = RegisterCategoryModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cat = Category(**data)
            cat.save()
            return redirect('ok')
        return render(request, 'todo/add_task.html', {'form': form})


class IndexPage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_task'] = Task.objects.order_by('-due_date')[:3]
        context['passed_task'] = Task.objects.get_passed_tasks()
        context['empty_cat'] = Category.objects.get_empty_categories()
        return context


def passed_tasks(request):  # not working
    passed = Task.objects.get_passed_tasks()
    return render(passed, 'index.html', {'passed': passed})
