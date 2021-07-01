from django.urls import path

from todo_project.forms_workshop.views import form_screen, form_send

urlpatterns = [
    path('', form_screen, name='form_screen'),
    path('form_send/', form_send, name='form_send')
]
