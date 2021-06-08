from django.urls import path
from todo_project.todo_app.views import login_screen, todo_add, todo_change_status_or_delete, \
    login_or_register, todo_screen, log_out

urlpatterns = [
    path('', todo_screen),
    path('todo_add', todo_add),
    path('todo_delete/<int:pk>', todo_change_status_or_delete),
    path('login_screen_login_or_register', login_or_register),
    path('login/', login_screen),
    path('logout', log_out)
]
