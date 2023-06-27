from rest_framework import serializers
from .models import AuthorModel,BookCategory,BookModel

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ('id','name','fname','date_of_birth','country')

class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = ('id','name')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('id','author','title','category','page','price')