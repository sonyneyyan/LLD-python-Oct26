
# Django REST Framework Study Material

## Table of Contents
- [Django REST Framework Study Material](#django-rest-framework-study-material)
  - [Table of Contents](#table-of-contents)
  - [1. Introduction to Django REST Framework ](#1-introduction-to-django-rest-framework-)
    - [Features:](#features)
  - [2. Installation ](#2-installation-)
  - [3. Setting Up Django REST Framework ](#3-setting-up-django-rest-framework-)
  - [4. Creating a Django App ](#4-creating-a-django-app-)
  - [5. Model Setup ](#5-model-setup-)
  - [6. Serializers ](#6-serializers-)
  - [7. Views (Function-Based and Class-Based) ](#7-views-function-based-and-class-based-)
    - [Function-Based View](#function-based-view)
    - [Class-Based View](#class-based-view)
  - [8. URLs and Routing ](#8-urls-and-routing-)
  - [9. Testing APIs ](#9-testing-apis-)
  - [10. Authentication and Permissions ](#10-authentication-and-permissions-)
  - [11. Pagination ](#11-pagination-)
  - [12. Filtering and Query Parameters ](#12-filtering-and-query-parameters-)
  - [13. Conclusion ](#13-conclusion-)
  - [14. Examples ](#14-examples-)
  - [Resources:](#resources)

---

## 1. Introduction to Django REST Framework <a name="introduction"></a>
Django REST Framework (DRF) is a powerful and flexible toolkit for building Web APIs. 
It makes it easy to create a RESTful API with Django, allowing for complete CRUD operations.

### Features:
- Authentication & Permissions
- Serialization
- Browsable API Interface
- Pagination, Filtering & Query Parameters

---

## 2. Installation <a name="installation"></a>

```bash
# Install Django and Django REST Framework
pip install django djangorestframework
```

---

## 3. Setting Up Django REST Framework <a name="setup"></a>

Add `rest_framework` to the `INSTALLED_APPS` in your `settings.py`:

```python
# settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'rest_framework',  # Add this
]
```

---

## 4. Creating a Django App <a name="creating-django-app"></a>

```bash
# Create a new Django app called 'books'
django-admin startapp books
```

Add the new app to `INSTALLED_APPS`:

```python
# settings.py
INSTALLED_APPS += ['books']
```

---

## 5. Model Setup <a name="model-setup"></a>

Define models in `books/models.py`:

```python
# books/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published_date = models.DateField()

    def __str__(self):
        return self.title
```

Run the migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 6. Serializers <a name="serializers"></a>

Create a serializer to convert model instances to JSON and vice versa.

```python
# books/serializers.py
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date']
```

---

## 7. Views (Function-Based and Class-Based) <a name="views"></a>

### Function-Based View

```python
# books/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
```

### Class-Based View

```python
# books/views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

---

## 8. URLs and Routing <a name="urls-and-routing"></a>

```python
# books/urls.py
from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
```

Include the app URLs in the main project `urls.py`:

```python
# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),
]
```

---

## 9. Testing APIs <a name="testing-apis"></a>

Start the Django development server:

```bash
python manage.py runserver
```

Use tools like `curl` or Postman to test the API:

```bash
curl http://127.0.0.1:8000/api/books/
```

---

## 10. Authentication and Permissions <a name="authentication-permissions"></a>

Add basic authentication:

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

Use API endpoints with authentication:

```bash
curl -u username:password http://127.0.0.1:8000/api/books/
```

---

## 11. Pagination <a name="pagination"></a>

Add pagination settings:

```python
# settings.py
REST_FRAMEWORK['DEFAULT_PAGINATION_CLASS'] = 'rest_framework.pagination.PageNumberPagination'
REST_FRAMEWORK['PAGE_SIZE'] = 5
```

---

## 12. Filtering and Query Parameters <a name="filtering"></a>

Use Django filters to filter API results:

```bash
pip install django-filter
```

Add filtering settings:

```python
# settings.py
INSTALLED_APPS += ['django_filters']

REST_FRAMEWORK['DEFAULT_FILTER_BACKENDS'] = [
    'django_filters.rest_framework.DjangoFilterBackend',
]
```

---

## 13. Conclusion <a name="conclusion"></a>

This study material provides a comprehensive overview of Django REST framework with step-by-step instructions for setting up, building, and testing APIs. It also introduces important topics such as authentication, pagination, and filtering.

Continue exploring the Django REST framework to add more advanced features like custom permissions, token authentication, and viewsets!

---

## 14. Examples <a name="Examples"></a>

- GET Request
```json 
[
    {
        "id": 1,
        "name": "Item 1",
        "description": "Description 1"
    },
    {
        "id": 2,
        "name": "Item 2",
        "description": "Description 2"
    }
]
```

- POST Request

```json 
{
    "name": "New Item",
    "description": "New Description"
}

```

- PUT Request

```json 
{
    "id": 1,
    "name": "Updated Item",
    "description": "Updated Description"
}

```

- DELETE Request

```json 
{
    "id": 1
}

```
---

## Resources:
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
- [Django Official Documentation](https://docs.djangoproject.com/)
