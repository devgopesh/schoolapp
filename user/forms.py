from django.contrib.auth.models import User
from django import forms
from .models import Assignment, Create

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class CreateForm(forms.ModelForm):
    class Meta:
        model = Create
        fields = ['title']


class AssignmentForm(forms.ModelForm):

    class Meta:
        model = Assignment
        fields = ['ques']