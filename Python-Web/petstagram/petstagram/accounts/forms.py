from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from petstagram.accounts.models import UserProfile
from petstagram.core.froms import BootstrapFormMixin


class LoginForm(BootstrapFormMixin, forms.Form):
    user = None

    username = forms.CharField(
        max_length=255,
    )

    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )

    def clean(self):
        self.user = authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )

        if not self.user:
            raise ValidationError('Username and/or password incorrect')

    def get_user(self):
        return self.user


class RegisterForm(BootstrapFormMixin, UserCreationForm):
    pass


class UserProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture', )
