from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import PythonCreateForm
from .models import Python


# Create your views here.
from ..core.mixins import UserGroupRequiredMixin


class IndexView(ListView):
    template_name = 'index.html'
    model = Python
    context_object_name = 'pythons'
    extra_context = {'page_name': 'home'}


class CreatePythonView(UserGroupRequiredMixin, CreateView):
    template_name = 'create.html'
    form_class = PythonCreateForm
    extra_context = {'page_name': 'create'}
    success_url = reverse_lazy('index')
