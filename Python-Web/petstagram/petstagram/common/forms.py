from django import forms

from petstagram.common.models import Comment
from petstagram.core.froms import BootstrapFormMixin
from petstagram.pets.models import Pet


class CommentForm(BootstrapFormMixin, forms.ModelForm):
    pet_pk = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Comment
        fields = ('comment', 'pet_pk')

    def save(self, commit=True):
        pet_pk = self.cleaned_data['pet_pk']
        pet = Pet.objects.get(pk=pet_pk)

        comment = Comment(
            comment=self.cleaned_data['comment'],
            pet=pet
        )

        if commit:
            comment.save()

        return comment
