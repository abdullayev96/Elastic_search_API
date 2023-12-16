from django.urls import path
from .views import ElasticAPI

urlpatterns = [
          path('elastic/', ElasticAPI.as_view())
]

