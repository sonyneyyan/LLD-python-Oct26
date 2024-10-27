from rest_framework import serializers

from library.models import Author, Book

# Basically the requests are coming from the user will be in json fromat
# We need to convert the json data into objects 

class bookSerializer(serializers.ModelSerializer):

    class Meta:  # this is the way to link the bookserializer to the book object
        model = Book # specify the class name
        fields = '__all__' # specify what are the fields we will be used by the serializer

class authorSerializer(serializers.ModelSerializer):

    class Meta:  # this is the way to link the bookserializer to the book object
        model = Author # specify the class name
        fields = '__all__' # specify what are the fields we will be used by the serializer
        
