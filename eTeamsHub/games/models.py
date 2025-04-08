from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to="images/game_logos/", blank=True,null=True)

    def __str__(self):
        return self.name
