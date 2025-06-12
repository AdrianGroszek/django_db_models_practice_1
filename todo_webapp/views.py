from django.shortcuts import render, get_object_or_404
from .models import Todo

# Create your views here.


def starting_page(request):
    return render(request, 'todo_webapp/index.html')


def todos_list_page(request):
    all_tasks = Todo.objects.all()
    return render(request, 'todo_webapp/todos_list.html', {
        "tasks": all_tasks
    })


def single_todo_page(request, slug):
    task = get_object_or_404(Todo, slug=slug)
    return render(request, 'todo_webapp/todo_detail.html', {
        "task": task
    })
