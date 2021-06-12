from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic import UpdateView

from .models import *


class MyUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ('username', 'full_name')


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Account
        fields = ('username', 'full_name')

