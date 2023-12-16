from django.urls import path
from .views import *
from knox import views as knox_views



urlpatterns = [
    path('register/',RegisterAPI.as_view()),
    path('login/',LoginAPI.as_view()),
    path('user/',UserAPI.as_view()),
]

