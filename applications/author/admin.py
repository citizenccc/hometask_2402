from django.contrib import admin

from applications.author.models import Author, Book

admin.site.register(Author)
admin.site.register(Book)
