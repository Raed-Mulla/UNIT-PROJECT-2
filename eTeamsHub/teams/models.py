from django.db import models
from games.models import Game

class Tournament(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='images/team_logos/', blank=True, null=True)
    games = models.ManyToManyField(Game, related_name="teams" , blank=True)
    tournaments = models.ManyToManyField(Tournament, related_name="teams", blank=True)

    def __str__(self):
        return self.name