from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings




class User(AbstractUser):
          username = models.CharField(blank=True, null=True, max_length=50, verbose_name="User nomi")
          email = models.EmailField(unique=True, verbose_name="Email addres")

          USERNAME_FIELD = 'email'
          REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

          def __str__(self):
                    return "{}".format(self.email)




class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    title = models.CharField(max_length=50, verbose_name="text nomi:")
    dob = models.DateField()
    address = models.CharField(max_length=255, verbose_name="address nomi:")
    country = models.CharField(max_length=50, verbose_name="davlat nomi:")
    city = models.CharField(max_length=50, verbose_name="shahar nomi:")
    zip = models.CharField(max_length=50)

    def __str__(self):
        return self.address


    class Meta:
          verbose_name = "Profile_"