from django.urls import path
from . import views

app_name = 'todolist'
urlpatterns = [
    path('', views.task, name='task'),
    path('index/', views.index, name='index'),
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('status/<task_id>', views.status_task, name='task_status'),
    path('edit/<task_id>', views.edit_task, name='edit_task'),
    path('about/', views.about, name='about')
]