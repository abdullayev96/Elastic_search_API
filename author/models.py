from django.db import models
from django.contrib.auth.models import User



class Elastic(models.Model):
      title  = models.TextField()
      answer = models.TextField()
      #user  = models.ForeignKey(User, on_delete=models.CASCADE)

      def __str__(self):
          return self.title


      class Meta:
          verbose_name = "Foydalanuvchi"


