from django.contrib import admin

from tryhello.models import Course, Enrollment, Student

# Register your models here.

admin.site.register(Student) # This is to register the student class to the admin panel 
admin.site.register(Course)
admin.site.register(Enrollment)