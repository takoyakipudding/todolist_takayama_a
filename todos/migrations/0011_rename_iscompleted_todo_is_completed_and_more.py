# Generated by Django 4.2.6 on 2024-07-08 07:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todos", "0010_todo_notes"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todo",
            old_name="isCompleted",
            new_name="is_completed",
        ),
        migrations.RenameField(
            model_name="todo",
            old_name="update_at",
            new_name="updated_at",
        ),
        migrations.AddField(
            model_name="todo",
            name="deadline_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="todo",
            name="deadline_time",
            field=models.TimeField(blank=True, null=True),
        ),
    ]