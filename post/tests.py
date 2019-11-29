from django.contrib.auth.models import User
from django.test import TestCase

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # first create a user
        testuser1 = User.objects.create_user(username="test", password="test@123")
        testuser1.save()

        # now create a blog post
        test_post = Post.objects.create(
            author=testuser1, title="test", body="hello my first test"
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        expected_author = f"{post.author}"
        expected_title = f"{post.title}"
        expected_body = f"{post.body}"
        self.assertEqual(expected_author, "test")
        self.assertEqual(expected_title, "test")
        self.assertEqual(expected_body, "hello my first test")
