from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Book

# Create your tests here.

class PostModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_book = Book.objects.create(
            user = test_user,
            title = 'Harry Potter',
            comment ='nice',
            type = 'Fantasy Fiction, Drama series of novels'
        )
        test_book.save()
        
    def test_blog_content(self):
        book = Book.objects.get(id=1)

        self.assertEqual(str(book.user), 'tester')
        self.assertEqual(book.title, 'Harry Potter')
        self.assertEqual(book.comment, 'nice')
        self.assertEqual(book.type, 'Fantasy Fiction, Drama series of novels')
