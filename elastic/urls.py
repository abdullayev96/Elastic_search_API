from django.urls  import path
from .views import *

urlpatterns  = [
     path('', index),
     path('search/', PublisherDocumentView.as_view({'get': 'list'})),

]
