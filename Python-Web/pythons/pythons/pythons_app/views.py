from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import PythonCreateForm
from .models import Python


# Create your views here.
from ..core.decorators import user_group_required


def index(req):
    pythons = Python.objects.all()
    return render(req, 'index.html', {'pythons': pythons, 'page_name': 'home'})


@user_group_required
def create(req):
    if req.method == 'GET':
        form = PythonCreateForm()

        context = {
            'form': form,
            'page_name': 'create',
        }

        return render(req, 'create.html', context)

    else:
        data = req.POST
        form = PythonCreateForm(data, req.FILES)

        if form.is_valid():
            python = form.save()
            python.save()
            return redirect('index')

        context = {
            'form': form,
            'page_name': 'create',
        }

        return render(req, 'create.html', context)
