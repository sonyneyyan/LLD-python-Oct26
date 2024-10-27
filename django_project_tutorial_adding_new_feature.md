
# Tutorial: Enhancing Your Django Project with New Functionality

## Introduction
This tutorial will guide you through adding new functionality to your Django project called **lld_project**. We will implement APIs to get information about books and authors. The new functionalities include:
1. Get a book by ID and return a JSON response
2. Get an author by ID and return a JSON response
3. Get all books and return a JSON response
4. Get all authors and return a JSON response

Additionally, we will validate the requests and responses and handle exceptions. This tutorial is designed to be straightforward and will provide examples along with best practices for implementation.

## Project Structure
Your project structure should look like this:
```
lld_project/
├── tryHello/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
└── library/
    ├── models.py
    ├── serializer.py
    ├── urls.py
    └── views.py
```

## Changes to `settings.py`
In your `settings.py` file, ensure that both `tryHello` and `library` applications are included in the `INSTALLED_APPS` section:

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tryHello',
    'library',
]
```

## URL Configuration
We will modify the URL configuration in `urls.py` of the `library` app to handle the new API endpoints:

### `library/urls.py`
```python
from django.urls import path
from library import views

urlpatterns = [
    path('createbook/', views.create_book),
    path('createauthor/', views.create_author),
    path('book/<int:book_id>/', views.get_book_by_id),
    path('author/<int:author_id>/', views.get_author_by_id),
    path('books/', views.get_all_books),
    path('authors/', views.get_all_authors),
]
```

## Implementing Views
### `library/views.py`
We'll add the views for the new functionalities. This includes methods to get books and authors by their IDs and to get all books and authors.

```python
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from library.models import Author, Book
from library.serializer import AuthorSerializer, BookSerializer

@api_view(['GET'])
def get_book_by_id(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    serializer = BookSerializer(book)
    return Response(serializer.data)

@api_view(['GET'])
def get_author_by_id(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    serializer = AuthorSerializer(author)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_authors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)
```

## Request and Response Validation
For all the new endpoints, we will validate the requests and ensure that appropriate responses are sent back to the client.

### Example Request
To get a book by ID, you would send a GET request to the following URL:
```
GET /api/book/1/
```

### Example Response
```json
{
    "id": 1,
    "title": "Example Book",
    "author": 1
}
```

## Exception Handling
Django REST Framework provides built-in mechanisms to handle exceptions, such as `get_object_or_404`. This method will return a 404 error if the requested object does not exist, ensuring that your API responds correctly in such cases.

## Best Practices
1. **Validation**: Always validate incoming data using serializers to ensure the integrity of your data.
2. **Error Handling**: Use built-in exception handling provided by Django REST Framework to simplify error responses.
3. **Documentation**: Comment your code and maintain proper documentation for your API endpoints to help other developers understand your project.
4. **Testing**: Write tests for your new functionalities to ensure everything works as expected.

## Diagram: API Flow for New Endpoints
```mermaid
graph TD;
    A[Client] -->|GET /api/book/{id}| B[Get Book by ID]
    A -->|GET /api/author/{id}| C[Get Author by ID]
    A -->|GET /api/books/| D[Get All Books]
    A -->|GET /api/authors/| E[Get All Authors]
    B --> F[Return Book Data]
    C --> G[Return Author Data]
    D --> H[Return All Books Data]
    E --> I[Return All Authors Data]
```

## Conclusion
You have successfully added new functionality to your Django project. By following the steps outlined in this tutorial, you can now retrieve book and author information through your API. Ensure to follow best practices in your development process to maintain a clean and efficient codebase.
