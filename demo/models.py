from typing import Tuple
from django.db import models
from django.db.models.base import Model


class BookNumber(models.Model):
	isbn_10 = models.CharField(max_length=10, blank=True)
	isbn_13 = models.CharField(max_length=13, blank=True)


class Book(models.Model):
	title = models.CharField(max_length=36, blank=False, unique=True)
	description = models.TextField(max_length=36, blank=True)

	price = models.DecimalField(default=0, max_digits=3, decimal_places=2)

	published = models.DateField(blank=True, null=True, default=None)
	is_published = models.BooleanField(default=False)

	cover = models.ImageField(upload_to='cover/', blank=True)

	# one-to-one relation
	number = models.OneToOneField(BookNumber,
										null=True,
										blank=True,
										on_delete=models.CASCADE)

	def __str__(self):
		return self.title


class Character(models.Model):
	name = models.CharField(max_length=30)
	# Book has one-to-many relation with character
	book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='characters')


class Author(models.Model):
	name = models.CharField(max_length=30)
	surname = models.CharField(max_length=30)

	# Book has many-to-may relation with author
	books = models.ManyToManyField(Book, related_name='authors')