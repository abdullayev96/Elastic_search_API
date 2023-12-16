from rest_framework import serializers
from .models import *




class CategorySerializer(serializers.ModelSerializer):
          class Meta:
              model  = Category
              fields  = ['id', 'name']





class AuthorSerializer(serializers.ModelSerializer):
          class Meta:
              model  = Author
              fields  = ['id', 'full_name', 'bio', 'image', 'created_at']





class BookSerializer(serializers.ModelSerializer):
          category = CategorySerializer()
          author  = AuthorSerializer()

          class Meta:
              model  = Book
              fields  = ['id', 'name', 'body', 'price','image','author', 'category', 'created_at']

