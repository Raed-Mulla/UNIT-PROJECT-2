from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    birth = models.DateField(null=True,blank=True)
    country = CountryField(blank_label='choose your country', null=True,blank=True)
    avatar = models.ImageField(upload_to="images/avatars/" , default="images/avatars/avatar.png")


    def __str__(self):
        return f"profile {self.user.username}"
