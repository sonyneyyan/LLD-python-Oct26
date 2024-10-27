from django.contrib import admin

# Register your models here.
from library.models import Author,Book

admin.site.register(Author)
admin.site.register(Book)