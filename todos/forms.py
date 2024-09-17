from django import forms
from .models import Todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TodoForm(forms.ModelForm):
    deadline_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    deadline_time = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time'}))
    isCompleted = forms.BooleanField(required=False)
    notification_lead_time = forms.IntegerField(required=False, widget=forms.Select(choices=[
        (0, 'なし'),
        (5, '5分前'),
        (10, '10分前'),
        (15, '15分前'),
    ]))

    class Meta:
        model = Todo
        fields = ['title', 'notes', 'deadline_date', 'deadline_time', 'isCompleted', 'notification_lead_time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['deadline_date'].initial = instance.deadline_date
            self.fields['deadline_time'].initial = instance.deadline_time
            self.fields['isCompleted'].initial = instance.isCompleted
            self.fields['notification_lead_time'].initial = instance.notification_lead_time

    def save(self, commit=True):
        todo = super().save(commit=False)
        todo.deadline_date = self.cleaned_data['deadline_date']
        todo.deadline_time = self.cleaned_data['deadline_time']
        todo.isCompleted = self.cleaned_data['isCompleted']
        todo.notification_lead_time = self.cleaned_data['notification_lead_time']
        if commit:
            todo.save()
        return todo

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')