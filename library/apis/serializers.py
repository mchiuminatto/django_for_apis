# apis/serializers.py

from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book  # which model we are using
        fields = ("title", "subtitle", "author", "isbn")  # which fields are we using

