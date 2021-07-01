from django.contrib import admin

# Register your models here.
from books_project.books_app.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
