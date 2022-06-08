import unittest
from django.test import Client, TestCase
from django.contrib.auth.models import User
from .models import Post, Comment



    

class TestTemplates(TestCase):
    """ gets the blog pages to make sure there is a positive response"""
    def test_get_home(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')            

if __name__ == "__main__":
    unittest.main()