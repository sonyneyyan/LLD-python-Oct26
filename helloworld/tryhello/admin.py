from django.contrib import admin

from tryhello.models import Course, Enrollment, Student

# Register your models here.

admin.site.register(Student) # This is to register the student class to the admin panel 
admin.site.register(Course)
admin.site.register(Enrollment)

class studentAdmin(admin.ModelAdmin):
    list_filter = ('name')
    list_display = ('name','age')
    list_editable = ('name')

# studentAdmin is related to Student table , this is done by the below code.

admin.site.register(Student,studentAdmin)