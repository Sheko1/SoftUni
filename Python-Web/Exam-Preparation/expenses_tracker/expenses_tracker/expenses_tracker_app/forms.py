from django import forms

from expenses_tracker.expenses_tracker_app.models import Profile, Expense


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name')


class CreateProfileForm(ProfileForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name')


class EditProfileForm(ProfileForm):
    pass


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = (
            'title',
            'description',
            'image_url',
            'price'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image_url'].label = 'Link to Image'


class CreateExpenseForm(ExpenseForm):
    pass


class EditExpenseForm(ExpenseForm):
    pass


class DeleteExpenseForm(ExpenseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = True
