from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator


class TodoForm(forms.Form):
    title = forms.CharField(
        label='Title',
        max_length=10,
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 2,
            }
        )
    )

    is_done = forms.BooleanField(label='Done', required=False)
