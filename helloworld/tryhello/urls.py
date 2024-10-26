from django.urls import path

from tryhello import views


urlpatterns = [path('hello/<str:name>',views.helloworld,name='hello')]