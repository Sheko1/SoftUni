from django.contrib import admin

# Register your models here.
from todo_project.todo_app.models import Todo

admin.site.register(Todo)
