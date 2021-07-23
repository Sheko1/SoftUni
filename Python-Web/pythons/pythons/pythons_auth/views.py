from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect


# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from pythons.pythons_auth.forms import LoginForm


class LoginUserView(LoginView):
    template_name = 'auth/login.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse('index')


class RegisterUserView(CreateView):
    form_class = UserCreationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('index')


def logout_view(req):
    logout(req)
    return redirect('index')
