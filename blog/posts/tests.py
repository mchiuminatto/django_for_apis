from django.test import TestCase

# bring the user model for testing
from django.contrib.auth import get_user_model


from .models import Post

# Create your tests here.


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        # create test user
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@testuser.com",
            password="secret"
        )

        # creates test post
        cls.post = Post.objects.create(
            author=cls.user,
            title="A good title",
            body="Nice body content"
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(str(self.post), "A good title")


