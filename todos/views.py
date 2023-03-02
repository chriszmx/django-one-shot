from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodoListForm, TodoItemForm

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


def todo_list_delete(request, id):
    name = TodoList.objects.get(id=id)
    if request.method == 'POST':
        name.delete()
        return redirect('todo_list')
    return render(request, 'todos/todo_list_delete.html')


def todo_item_create(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('todo_list_detail', id=item.list.id)

    else:
        form = TodoItemForm()

    context = {
        'form': form,
    }

    return render(request, 'todos/item_create.html', context)


def todo_item_update(request, id):
    todo_item = get_object_or_404(TodoItem, id=id)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            return redirect('todo_list_detail', id=id)
    else:
        form = TodoItemForm(instance=todo_item)

    context = {
        'todo_item': todo_item,
        'form': form,
        }
    return render(request, 'todos/todo_list_update.html', context)
