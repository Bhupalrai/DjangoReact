from django.db.models import fields
from rest_framework import serializers
from .models import Author, Book, BookNumber, Character

class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = ['id', 'isbn_10', 'isbn_13']


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name', 'book']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'surname']


class BookSerializer(serializers.ModelSerializer):

    # Use other serialized objects to obtain full detail
    number = BookNumberSerializer(many=False)
    characters = CharacterSerializer(many=True)
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'published', 'is_published',
                'number', 'characters', 'authors']

# Sometime we do not require all details
class BookMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title']