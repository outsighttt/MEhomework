from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=20
    )
    last_name = forms.CharField(
        max_length=30
    )
