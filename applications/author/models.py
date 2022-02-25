from django.contrib.auth import get_user_model
from django.db import models

# User = get_user_model()

class Author(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(   )
    place_of_birth = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}, {self.last_name}"

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True, related_name='book')
    title = models.CharField(max_length=200)
    date_of_publish = models.DateTimeField()
    picture = models.ImageField(upload_to='')
    price = models.DecimalField(decimal_places=1, max_digits=10)
    is_bestseller = models.BooleanField()

    def __str__(self):
        return self.title

