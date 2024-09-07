from django.db import models
from django.contrib.auth.models import User
from fcm_django.models import FCMDevice as BaseFCMDevice

class FCMDevice(BaseFCMDevice):
    owner = models.ForeignKey(User, related_name='fcm_devices_todos', on_delete=models.CASCADE)
    device_registration_id = models.TextField(unique=True)
    renamed_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'FCM Device'
    
    def send_push_notification(user, title, message):
        devices = FCMDevice.objects.filter(owner=user, active=True)
        for device in devices:
            device.send_message(title=title, body=message)

class Todo(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField('Created', auto_now_add=True)
    update_at = models.DateTimeField('Updated', auto_now=True)
    isCompleted = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    notes = models.TextField(blank=True, null=True)
    deadline_date = models.DateField(blank=True, null=True)
    deadline_time = models.TimeField(blank=True, null=True)
    notification_lead_time = models.IntegerField(default=0)

    def __str__(self):
        return self.title
