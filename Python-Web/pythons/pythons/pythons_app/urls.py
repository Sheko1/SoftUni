from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('create/', views.CreatePythonView.as_view(), name="create"),
]
