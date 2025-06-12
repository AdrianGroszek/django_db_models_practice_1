from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name='starting-page'),
    path('todos', views.todos_list_page, name='todos-list-page'),
    path('todos/<slug:slug>', views.single_todo_page, name='single-todo-page')
]
