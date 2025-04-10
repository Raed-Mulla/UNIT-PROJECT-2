from django.db import models
from teams.models import Team

class Player(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/players/', blank=True, null=True)
    game_name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')

    def __str__(self):
        return self.name