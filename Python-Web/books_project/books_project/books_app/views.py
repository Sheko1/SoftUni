from django.shortcuts import render, redirect

# Create your views here.
from books_project.books_app.forms import BookForm
from books_project.books_app.models import Book


def show_book_form(request, form, template_name):
    context = {
        'form': form
    }

    return render(request, template_name, context)


def index(request):
    books = sorted(Book.objects.all(), key=lambda x: x.id)
    context = {
        'books': books
    }

    return render(request, 'index.html', context)


def create_book(request):
    if request.method == 'GET':
        form = BookForm()

        return show_book_form(request, form, 'create.html')

    else:
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

        return show_book_form(request, form, 'create.html')


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == 'GET':
        form = BookForm(initial=book.__dict__)

        return show_book_form(request, form, 'edit.html')

    else:
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('index')

        return show_book_form(request, form, 'edit.html')
