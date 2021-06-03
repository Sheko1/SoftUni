from django.shortcuts import render

# Create your views here.
from todo_project.todo_app.models import Todo


def index(req):
    context = {'todos': Todo.objects.all()}
    return render(req, "index.html", context=context)
