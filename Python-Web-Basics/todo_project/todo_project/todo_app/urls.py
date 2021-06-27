from django.urls import path

from todo_project.todo_app.views import index, create, update, delete

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create_todo'),
    path('update/<int:pk>', update, name='update_todo'),
    path('delete/<int:pk>', delete, name='delete_todo'),
]
