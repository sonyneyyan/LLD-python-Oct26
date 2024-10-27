from django.urls import path

from library import views

urlpatterns = [
    path('createBook/',views.createBook,name='createbook'),
    path('createAuthor/',views.createAuthor,name='createauthor'),
    path('book/<int:book_id>/', views.get_book_by_id, name='get_book_by_id'),
    path('author/<int:author_id>/', views.get_author_by_id, name='get_author_by_id'),
    path('books/', views.get_all_books, name='get_all_books'),
    path('authors/', views.get_all_authors, name='get_all_authors'),
]
