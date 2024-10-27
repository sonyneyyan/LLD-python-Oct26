from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from library.serializer import authorSerializer, bookSerializer
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