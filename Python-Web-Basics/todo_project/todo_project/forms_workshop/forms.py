from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, EmailValidator


def name_validator(value):
    if value[0] != value[0].upper():
        raise ValidationError('The name must start with an uppercase letter.')


def age_validator(value):
    if value < 0:
        raise ValidationError('The age cannot be less than zero.')


def password_validator(value):
    if any([not x.isalnum() for x in value]):
        raise ValidationError('Enter a valid password.')


def bot_catcher(value):
    if value:
        raise ValidationError('This form was created by a bot')


class UserForm(forms.Form):
    name = forms.CharField(
        validators=[
            MinLengthValidator(6),
            name_validator,
        ]
    )

    age = forms.IntegerField(
        widget=forms.NumberInput,
        validators=[
            age_validator,
        ]
    )

    email = forms.EmailField(
        validators=[
            EmailValidator(),
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput,
        validators=[
            MinLengthValidator(8),
            password_validator,
        ]
    )

    text = forms.CharField(
        widget=forms.Textarea,
    )

    bot_catcher = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        validators=[
            bot_catcher
        ]
    )
