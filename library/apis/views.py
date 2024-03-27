
# apis/views.py
from rest_framework import generics
from books.models import Book
from .serializers import BookSerializer


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()  # get all books available from books application database
    serializer_class = BookSerializer  # render book list into json