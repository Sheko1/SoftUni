from expenses_tracker.expenses_tracker_app.models import Profile, Expense


def get_profile():
    profile = Profile.objects.first()

    if profile:
        expenses = Expense.objects.all()
        profile.budget_left = f'{profile.budget - sum(e.price for e in expenses):.2f}'

    return profile
