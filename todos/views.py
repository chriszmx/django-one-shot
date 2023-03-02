from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList
from todos.forms import TodoListForm

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


def todo_list_create(request):
    form = TodoListForm()
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            todo_list = form.save()
            return redirect('todo_list_detail', todo_list.id)
    context = {
        'form': form,
        }
    return render(request, 'todos/todo_list_create.html', context)


def todo_list_update(request, id):
    title_edit = get_object_or_404(TodoList, id=id)
    if request.method == 'POST':
        form = TodoListForm(request.POST, instance=title_edit)
        if form.is_valid():
            form.save()
            return redirect('todo_list_detail', id=id)
    else:
        form = TodoListForm(instance=title_edit)

    context = {
        'title_edit': title_edit,
        'form': form,
    }
    return render(request, 'todos/todo_list_update.html', context)
