from django.contrib import admin

# Register your models here.
from books_rest.books_api.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
