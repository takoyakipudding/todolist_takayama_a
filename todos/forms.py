from django import forms
from .models import Todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'notes'] 