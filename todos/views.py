from django.shortcuts import render, get_object_or_404
from todos.models import TodoList

# Create your views here.


def todo_list(request):
    todo_lists = TodoList.objects.all()
    context = {
        'todo_lists': todo_lists,
    }
    return render(request, 'todos/list.html', context)


def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    context = {'todo_lists': todo_list}
    return render(request, 'todos/todo_list_detail.html', context)
