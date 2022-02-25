
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from applications.author.models import Author, Book
from applications.author.serializers import AuthorSerializer, BookSerializer

# 1 method
# @api_view(['GET',])
# def book_list(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)

# 2 method
# from rest_framework.views import APIView
#
# class BookView(APIView):
#     def get(self, request):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# 3 method
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
