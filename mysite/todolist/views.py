from django.shortcuts import render, redirect
from .models import Task
from .form import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ("Task Added sucessfully....!!!"))
        return redirect('todolist:task')
    else:
        all_tasks = Task.objects.all()
        return render(request, 'task.html', context={'all_tasks': all_tasks})
    # context_dict = {'welcome_task': "Welcome to Task page"}
    # return render(request, 'task.html', context=context_dict)
    # return render(request, 'task.html', context={'all_tasks': all_tasks})
    # all_tasks = Task.objects.all()


def delete_task(request, task_id):
    tasks_obj = Task.objects.get(pk=task_id)
    tasks_obj.delete()
    return redirect('todolist:task')


def index(request):
    context_dict = {'welcome_home': 'Welcome to MySite'}
    return render(request, 'index.html', context=context_dict)


def edit_task(request, task_id):
    if request.method == 'POST':
        tasks_obj = Task.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=tasks_obj)
        if form.is_valid():
            form.save()
        messages.success(request, ("Task Updated sucessfully....!!!"))
        return redirect('todolist:task')
    else:
        tasks_obj = Task.objects.get(pk=task_id)
        return render(request, 'edit.html', context={'tasks_obj': tasks_obj})


def status_task(request, task_id):
    tasks_obj = Task.objects.get(pk=task_id)
    tasks_obj.done = not tasks_obj.done
    tasks_obj.save()
    return redirect('todolist:task')


def about(request):
    context_dict = {'welcome_about': "Welcome to About page"}
    return render(request, 'about.html', context=context_dict)
