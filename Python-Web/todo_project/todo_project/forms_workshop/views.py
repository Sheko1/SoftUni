from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from todo_project.forms_workshop.forms import UserForm


def form_screen(request):
    context = {
        'form': UserForm
    }

    return render(request, 'from_workshop/forms.html', context)


def form_send(request):
    form = UserForm(request.POST)

    if form.is_valid():
        fields = ['name', 'age', 'email', 'password', 'text']
        result = 'VALIDATION SUCCESS\n'

        for field in fields:
            result += f'{field}: {form.cleaned_data[field]}\n'
        return HttpResponse(result, content_type='text/plain')

    context = {
        'form': form
    }

    return render(request, 'from_workshop/forms.html', context)
