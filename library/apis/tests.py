# apis/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Book


class APITests(APITestCase):

    @classmethod
    def setUpTestData(cls):  # creates a book
        cls.book = Book.objects.create(
        title="Django for APIs",
        subtitle="Build web APIs with Python and Django",
        author="William S. Vincent",
        isbn="9781735467221",
        )

    def test_api_listview(self):
        response = self.client.get(reverse("book_list"))  # checks the named url is being used
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # check status code
        self.assertEqual(Book.objects.count(), 1)  # check object count
        self.assertContains(response, self.book)  # checks response type