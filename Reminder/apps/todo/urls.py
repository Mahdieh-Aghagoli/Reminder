from django.urls import include, path

from apps.todo.views import TaskList, TaskDetail, CategoryList, CategoryTaskList, AddTask, AddCategory, OrderedTaskList

urlpatterns = [
    path('tasks/', include([
        path('', TaskList.as_view(), name='task_list'),
        path('<int:pk>/', TaskDetail.as_view(), name='task_detail'),
        path('o_task_list.html/', OrderedTaskList.as_view(), name='o_detail'),
    ])),
    path('categories/', include([
        path('', CategoryList.as_view(), name='categories'),
        path('<int:pk>/', CategoryTaskList.as_view()),
    ])),
    path('add_task/', AddTask.as_view(), name='add_task'),
    path('add_categoty/', AddCategory.as_view(), name='add_cat')
]
