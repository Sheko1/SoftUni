from django.contrib import admin

# Register your models here.
from python_web_exam.recipes.models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'ingredients', 'time')
