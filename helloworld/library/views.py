from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from library.utils import get_object
from library.serializer import authorSerializer, bookSerializer
from library.models import Book,Author
# Create your views here.
# All the rest related code will be handled in the views.py file

@api_view(['POST'])
def createBook(request):
    
    book_serializer = bookSerializer(data=request.data)

    if book_serializer.is_valid():
        book_serializer.save()
        return Response(book_serializer.data,status=status.HTTP_201_CREATED)
    return Response(book_serializer.errors,status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST'])
def createAuthor(request):
    author_serializer = authorSerializer(data=request.data)

    if author_serializer.is_valid():
        author_serializer.save()
        return Response(author_serializer.data,status=status.HTTP_201_CREATED)
    return Response(author_serializer.errors,status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_book_by_id(request, book_id):
    book = get_object(Book, id=book_id)  # Pass id as a keyword argument.
    if isinstance(book, Response):  # Check if book is a Response object.
        return book  # Return the 404 response if not found.
    serializer = bookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_author_by_id(request, author_id):
    author = get_object(Author, id=author_id)  # Corrected to use Author model.
    if isinstance(author, Response):  # Check if author is a Response object.
        return author  # Return the 404 response if not found.
    serializer = authorSerializer(author)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_books(request):
    books = Book.objects.all()
    serializer = bookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_authors(request):
    authors = Author.objects.all()  # Corrected to use Author model.
    serializer = authorSerializer(authors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)