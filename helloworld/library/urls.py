from django.urls import path

from library import views

urlpatterns = [
    path('createBook/',views.createBook,name='createbook'),
    path('createAuthor/',views.createAuthor,name='createauthor'),
]
