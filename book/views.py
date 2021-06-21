from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# Create your views here.
 
class BooksList(generics.ListCreateAPIView):
     queryset = Book.objects.all()
     serializer_class = BookSerializer

class BooksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
