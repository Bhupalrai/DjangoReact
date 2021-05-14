from django import views
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import serializers, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response 

from .models import Book
from .serializers import BookMiniSerializer, BookSerializer


def first(request):
    books = Book.objects.all()
    return render(request, 'first_temp.html', {'books': books})


class BookViewSet(viewsets.ModelViewSet):

    # Retrieve only few part when listing all books
    # serializer_class = BookSerializer
    serializer_class = BookMiniSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)

    # Retrieve book's full detail
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)
