from django.contrib import admin

# Register your models here.
from expenses_tracker.expenses_tracker_app.models import Profile, Expense


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    pass
