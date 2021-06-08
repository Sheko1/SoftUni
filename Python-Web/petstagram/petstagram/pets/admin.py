from django.contrib import admin

# Register your models here.
from petstagram.pets.models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'age')


admin.site.register(Pet, PetAdmin)
