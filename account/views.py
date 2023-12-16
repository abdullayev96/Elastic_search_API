from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from django.contrib.auth.models import User
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from django.conf import settings
from django.middleware import csrf

from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken




class RegisterAPI(GenericAPIView):
      serializer_class = RegisterSerializer

      def post(self, request, *args, **kwargs):
          try:
             serializer = self.serializer_class(data=request.data)
             serializer.is_valid(raise_exception=True)
             user  = serializer.save()

             return Response({"user":UserSerializer(
                       user, context=self.get_serializer_context()).data,
                       "token":AuthToken.objects.create(user)[1]})

          except Exception as e:
                 print(e)


          return  Response({"status":status.HTTP_400_BAD_REQUEST})


# class LoginAPI(APIView):
#       def post(self, request):
#           username = request.data.get('username')
#           password = request.data.get('password')
#
#           user = authenticate(username=username, password=password)
#
#           if user is not None:
#                     token, created = Token.objects.get_or_create(user=user)
#                     response = {
#                               "status": status.HTTP_200_OK,
#                               "message": "success", "token": {"Token": token.key, }
#                     }
#
#                     return Response(response, status=status.HTTP_200_OK)
#
#           else:
#                     response = {"status": status.HTTP_401_UNAUTHORIZED,
#                                 "message": "Invalid username or Password"}
#                     return Response(response, status=status.HTTP_401_UNAUTHORIZED)
#


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh_token': str(refresh),
        'access_token': str(refresh.access_token),
    }



class LoginAPI(APIView):
    def post(self, request):
        try:
           username = request.data.get('username', None)
           password = request.data.get('password', None)

           user = authenticate(username=username, password=password)

           data = get_tokens_for_user(user)
           return Response({'data': data})

        except Exception as e:
            print(e)


        return  Response({'status':status.HTTP_404_NOT_FOUND})



class UserAPI(ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

