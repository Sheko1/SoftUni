from django import forms

from petstagram.core.froms import BootstrapFormMixin
from petstagram.pets.models import Pet


class CreatePetForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ('user', )


class EditPetForm(CreatePetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].disabled = True
