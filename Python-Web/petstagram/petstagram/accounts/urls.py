from django.urls import path, include
from petstagram.accounts import signals

from petstagram.accounts.views import login_user, logout_user, register_user, profile_details

urlpatterns = [
    path('login/', login_user, name='login user'),
    path('logout/', logout_user, name='logout user'),
    path('register/', register_user, name='register user'),
    path('profile/', profile_details, name='profile details'),
]
