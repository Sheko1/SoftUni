from django.urls import path
from todo_project.todo_app.views import index

urlpatterns = [
    path('', index)
]
