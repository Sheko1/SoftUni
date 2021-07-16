from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    user = None

    username = forms.CharField(
        max_length=150
    )

    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    def clean(self):
        self.user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])

        if not self.user:
            raise ValidationError('Wrong username or password!!')

    def save(self):
        return self.user
