from django.urls import path
from todo_project.todo_app.views import index, todo_add, todo_delete

urlpatterns = [
    path('', index),
    path('todo_add', todo_add),
    path('todo_delete/<int:pk>', todo_delete)
]
