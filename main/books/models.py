from django.db import models

# Create your models here.
class BookModel(models.Model):
    name = models.CharField()
    BookContent = models.FileField()

class AuthorsModel(models.Model):
    author = models.CharField()
    bio = models.TextField()
    books = models.ManyToManyField(BookModel)