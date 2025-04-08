from django.db import models
from django.contrib.auth.models import User
from teams.models import Team


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="images/avatars/" , default="images/avatars/avatar.png")
    favorite_team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)


    def __str__(self):
        return f"profile {self.user.username}"
