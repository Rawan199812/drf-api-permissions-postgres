from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.
 
class BooksList(generics.ListCreateAPIView):
     permission_classes = (IsAuthenticatedOrReadOnly,)

     queryset = Book.objects.all()
     serializer_class = BookSerializer

class BooksDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)

    queryset = Book.objects.all()
    serializer_class = BookSerializer
