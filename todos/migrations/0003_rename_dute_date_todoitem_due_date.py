# Generated by Django 4.1.7 on 2023-03-01 16:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todos", "0002_todoitem"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todoitem",
            old_name="dute_date",
            new_name="due_date",
        ),
    ]
