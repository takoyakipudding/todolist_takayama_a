# Generated by Django 4.2.6 on 2024-07-13 01:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("fcm_django", "0011_fcmdevice_fcm_django_registration_id_user_id_idx"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("todos", "0012_todo_notification_lead_time"),
    ]

    operations = [
        migrations.CreateModel(
            name="FCMDevice",
            fields=[
                (
                    "fcmdevice_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="fcm_django.fcmdevice",
                    ),
                ),
                ("device_registration_id", models.TextField(unique=True)),
                ("renamed_active", models.BooleanField(default=True)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fcm_devices_todos",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "FCM Device",
            },
            bases=("fcm_django.fcmdevice",),
        ),
    ]
