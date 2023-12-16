from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import  ListAPIView
from rest_framework.views import APIView, Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import *
from  django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters
from .paginations import ListPagination

######  Category API CRUD
#
# class  CategoryAPI(APIView):
#
#      def get(self, request):
#            try:
#                  cat = Category.objects.all()
#                  serializers = CategorySerializer(cat, many=True)
#                  return Response({"data":serializers.data})
#
#            except Exception as e:
#                  print(e)
#
#
#            return Response({"status":status.HTTP_400_BAD_REQUEST})
#
#      def post(self, request):
#          try:
#                data = request.data
#                serializer  = CategorySerializer(data=data)
#                if serializer.is_valid(raise_exception=True):
#                      serializer.save()
#
#                return Response({"data":serializer.data, "status":status.HTTP_201_CREATED})
#
#
#          except Exception as e:
#                print(e)
#
#
#          return Response({"status":status.HTTP_400_BAD_REQUEST})
#
#
#
# class DetailCategory(APIView):
#      def get(self, request, pk=None):
#           try:
#               cat = Category.objects.get(id=pk)
#               serializers = CategorySerializer(cat)
#               return Response({"data": serializers.data})
#
#           except Exception as e:
#                     print(e)
#
#           return Response({"status": status.HTTP_400_BAD_REQUEST})
#
#      def put(self, request, pk=None):
#          try:
#                cat  = Category.objects.get(id=pk)
#                serializer = CategorySerializer(cat, data=request.data)
#                if serializer.is_valid(raise_exception=True):
#                     serializer.save()
#                     return Response({"data":serializer.data})
#
#          except Exception as e:
#                    print(e)
#
#          return Response({"status":status.HTTP_400_BAD_REQUEST})
#
#      def delete(self, request, pk=None):
#           try:
#                cat = Category.objects.get(id=pk)
#                cat.delete()
#           except Exception as e:
#                     print(e)
#
#           return Response(status=status.HTTP_204_NO_CONTENT)

class BookAPI(ListAPIView):
      queryset = Book.objects.all()
      serializer_class = BookSerializer

      # filter_backends = [DjangoFilterBackend]
      # filterset_fields = ['category', 'author']

      search_fields = ['name', 'body']

      filter_backends = [filters.SearchFilter]
      pagination_class = ListPagination

      permission_classes = [IsAuthenticated]





