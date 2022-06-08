from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

class UserTest(TestCase):
    def user_test(self):
        """ creates a user """
        user_test = User.objects.create_user(
            username='user1', password='userpass'
            )
        self.post = Post.objects.create(title='test', author=user_test)
        self.comment = Comment.objects.create(
            body='Test Comment', post=self.post
            )
        self.client.login(username="user1", password="userpass")