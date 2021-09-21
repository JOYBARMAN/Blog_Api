from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User


class BlogTests(TestCase):
    @classmethod

    def setUpTestData(cls):
        testuser1=User.objects.create_user(username='testuser1',password='abc123') #Create a user
        testuser1.save()

    #   Craete a blog post
        test_post=Post.objects.create(
            author=testuser1,title='Blog Title',body='Body content')
        test_post.save()

    def test_blog_content(self):
        post=Post.objects.get(id=1)
        author=f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author,'testuser1')
        self.assertEqual(title, 'Blog Title')
        self.assertEqual(body, 'Body content')





