from rest_framework import serializers
from .models import Elastic



class ElasticSerializer(serializers.ModelSerializer):
      class Meta:
          model = Elastic
          fields = ['title']


