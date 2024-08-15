from django.contrib import admin
from .models import BookModel, AuthorsModel

admin.site.register(BookModel)
admin.site.register(AuthorsModel)
# Register your models here.
