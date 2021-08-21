from django.urls import path

from books_rest.books_api.views import ListBooksView, DetailsBookView

urlpatterns = (
    path('books/', ListBooksView.as_view(), name='books list'),
    path('books/<int:pk>', DetailsBookView.as_view(), name='book details'),
)
