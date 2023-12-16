# from django.urls  import path
# from .views import *
#
# from rest_framework import routers
#
# router = routers.SimpleRouter(trailing_slash=False)
# router.register('search/', ArticleDocumentView, basename='search'),
#
# urlpatterns = router.urls

from django.urls import path
from rest_framework import routers

from  .views import ArticleDocumentView

router = routers.SimpleRouter(trailing_slash=False)

router.register('article-search/', ArticleDocumentView, basename='article-search')


urlpatterns = router.urls