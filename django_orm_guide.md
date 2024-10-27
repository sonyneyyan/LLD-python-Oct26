# Django ORM (Object-Relational Mapping)

Django's Object-Relational Mapping (ORM) system is a powerful feature that enables you to interact with your database using Python code instead of raw SQL queries. This document provides an overview of Django ORM, its benefits, and some common operations.

---

## What is Django ORM?

Django ORM is a component of the Django framework that allows you to define your data models as Python classes. These models are then mapped to database tables, enabling you to perform CRUD (Create, Read, Update, Delete) operations without writing raw SQL.
<img width="580" alt="Screenshot 2024-10-27 at 16 12 51" src="https://github.com/user-attachments/assets/f94ad494-5b5d-401b-82a9-b8c0800a6ce1">

---

## Key Features of Django ORM

1. **Model Definition**: Define your database schema as Python classes by creating models that inherit from `django.db.models.Model`.

2. **QuerySet API**: A powerful API that allows you to create complex queries using method chaining.

3. **Database Migrations**: Automatically tracks changes to your models and generates database migrations.

4. **Cross-Database Support**: Works with multiple database backends, including PostgreSQL, MySQL, SQLite, and Oracle.

5. **Built-in Methods**: Includes various built-in methods for filtering, ordering, and aggregating data.

---

## Defining a Model

Here's a simple example of how to define a model in Django:

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
```

### Explanation of the Model:
- **Author Model**: Represents an author with a `name` field.
- **Book Model**: Represents a book with a `title` field and a foreign key relationship to the `Author`.

---

## Basic CRUD Operations

### Creating an Object

```python
# Creating an Author instance
author = Author.objects.create(name="J.K. Rowling")

# Creating a Book instance
book = Book.objects.create(title="Harry Potter", author=author)
```

### Reading Objects

```python
# Get a single object by ID
book = Book.objects.get(id=1)

# Get all books
all_books = Book.objects.all()

# Filtering
filtered_books = Book.objects.filter(author__name="J.K. Rowling")
```

### Updating an Object

```python
# Updating a book's title
book = Book.objects.get(id=1)
book.title = "Harry Potter and the Philosopher's Stone"
book.save()
```

### Deleting an Object

```python
# Deleting a book
book = Book.objects.get(id=1)
book.delete()
```

---

## QuerySet Methods

- **`filter()`**: Returns a new QuerySet containing objects that match the given criteria.
- **`exclude()`**: Returns a new QuerySet containing objects that do not match the given criteria.
- **`order_by()`**: Returns a new QuerySet that is ordered by the specified field(s).
- **`aggregate()`**: Used to compute values over a QuerySet, such as counts, averages, etc.
- **`annotate()`**: Adds calculated fields to the QuerySet.

---

## Migrations

To create database tables based on your models, you need to create and apply migrations:

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### Migration Process Flowchart

```plaintext
+-----------------+
| Define Models   |
+-----------------+
          |
          v
+-----------------+
| Create Migrations|
+-----------------+
          |
          v
+-----------------+
| Apply Migrations |
+-----------------+
```

---

## Summary

Django's ORM makes database interactions straightforward and efficient, allowing you to work with databases using Python's object-oriented paradigms. It abstracts away much of the complexity of raw SQL, making it easier to develop and maintain your applications.

### Example Flow of a Django ORM Operation

1. **Define the Model**: Create a model class.
2. **Create an Object**: Use the `create()` method to save an instance.
3. **Retrieve Data**: Use `get()` or `filter()` to retrieve data.
4. **Update Data**: Modify the instance and call `save()`.
5. **Delete Data**: Call `delete()` on the instance.

---

For further reading, refer to the [Django Documentation](https://docs.djangoproject.com/en/stable/topics/db/models/).

Feel free to reach out if you have specific questions or topics within Django ORM you'd like to discuss!
