from django.db import models
from django.utils import timezone

# Create your models here.


class TodoList(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    task = models.CharField(max_length=100)
    due_date = models.DateTimeField(
        default=timezone.now,
        null=True,
        blank=True
        )
    is_completed = models.BooleanField(default=False)
    list = models.ForeignKey(
        TodoList,
        on_delete=models.CASCADE,
        related_name='items',
        )

    def __str__(self):
        return self.task
