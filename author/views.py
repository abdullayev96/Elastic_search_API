from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.views import status
from .serializers import ElasticSerializer

import random
import string




def generate_random_string(length):
          characters = string.ascii_letters + string.digits
          answer = ''.join(random.choice(characters) for _ in range(length))
          return answer


class ElasticAPI(APIView):
          def post(self, request):
              try:
                  answer = generate_random_string(10000)
                  serializer = ElasticSerializer(data=request.data, context={'request': self.request})
                  serializer.is_valid(raise_exception=True)
                  serializer.save(answer=answer)
                  return Response({"true":answer})


              except Exception as e:
                        print(e)



