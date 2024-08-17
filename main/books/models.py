from django.db import models

# Create your models here.
class BookModel(models.Model):
    author = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    bookContent = models.FileField(upload_to='Book')

class AuthorsModel(models.Model):
    author = models.CharField(max_length=100)
    bio = models.TextField(max_length=500)
    books = models.ManyToManyField(BookModel)