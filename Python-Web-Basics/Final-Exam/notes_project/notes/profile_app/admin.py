from django.contrib import admin

# Register your models here.
from notes.profile_app.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
