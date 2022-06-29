import unittest
from django.test import Client, TestCase
from django.contrib.auth.models import User
from .models import Post, Comment



class TestUser(unittest.TestCase):
    def test_user(self):
        """ creates a user, test post and comment """
        test_user = User.objects.create_user(
            username='user20', password='userpass'
            )
        self.post = Post.objects.create(title='test20', author=test_user)
        self.comment = Comment.objects.create(
            body='Test Comment', post=self.post
            )  

class TestTemplates(TestCase):
    """ gets the blog pages to make sure there is a positive response"""
    def test_get_home(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')            

    def test_get_post_detail(self):
        post_list = Post.objects.all()
        for post in post_list:
            c = Client()
            response = c.get(f'/post_detail/{self.post.id}')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'post_detail.html')

    def test_get_search(self):
        c = Client()
        response = c.get('/search')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')   

    def test_edit_comment_page(self):
        
        comments = Comment.objects.all()
        for comment in comments:
            c = Client()
            response = c.get(f'/edit_comment/{self.comment.id}')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'edit_comment.html')         

if __name__ == "__main__":
    unittest.main()