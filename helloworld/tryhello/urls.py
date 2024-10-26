from django.urls import path

from tryhello import views


urlpatterns = [path('hello/',views.helloworld,name='hello')]