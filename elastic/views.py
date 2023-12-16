from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse
import requests
import json
from .models import *

from .documents import *
from .serializers import *

from django_elasticsearch_dsl_drf.filter_backends import (
          FilteringFilterBackend,
          CompoundSearchFilterBackend
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
          FilteringFilterBackend,
          OrderingFilterBackend,
)


def generate_random_data():
          url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=API_KEY'
          r = requests.get(url)
          payload = json.loads(r.text)
          count = 1

          # print (payload)
          print("type of payload is: ", type(payload))
          for data in payload:
             print(data)
             try:
                  ElasticDemo.objects.create(
                      title=data['title'],
                     content=data['content']
                 )

             except Exception as e:
                       print(e)


def index(request):
          generate_random_data()
          return JsonResponse({'status': 200})
          # return HttpResponse("Hello, the world")


class PublisherDocumentView(DocumentViewSet):
          document = NewsDocument
          serializer_class = NewsDocumentSerializer
          lookup_field = 'first_name'
          fielddata = True
          filter_backends = [
                    FilteringFilterBackend,
                    OrderingFilterBackend,
                    CompoundSearchFilterBackend,
          ]

          search_fields = (
                    'title',
                    'content',
          )
          multi_match_search_fields = (
                    'title',
                    'content',
          )
          filter_fields = {
                    'title': 'title',
                    'content': 'content',
          }
          ordering_fields = {
                    'id': None,
          }
          ordering = ('id',)