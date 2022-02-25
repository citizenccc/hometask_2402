
from rest_framework import serializers

from applications.author.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('id')
        representation['category'] = AuthorSerializer(Author.objects.get(book=instance.id)).data

        return representation