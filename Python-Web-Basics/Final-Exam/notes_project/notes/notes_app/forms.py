from django import forms

from notes.notes_app.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = (
            'title',
            'content',
            'image_url'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image_url'].label = 'Link to Image'


class NoteCreateForm(NoteForm):
    pass


class NoteEditForm(NoteForm):
    pass


class NoteDeleteForm(NoteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = True
