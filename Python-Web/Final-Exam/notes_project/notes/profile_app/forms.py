from django import forms

from notes.profile_app.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image_url'].label = 'Link to Profile Image'
