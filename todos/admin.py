from django.contrib import admin
from todo.models import TodoList

# Register your models here.


@admin.register(TodoList)
class TodoList(admin.ModelAdmin):
    list_display = (
        'name',
        'id',
    )
