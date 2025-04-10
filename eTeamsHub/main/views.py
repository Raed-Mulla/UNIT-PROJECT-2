from django.shortcuts import render
from teams.models import Team
from games.models import Game

def home(request):
    teams = Team.objects.all()[:3]
    games = Game.objects.all()[:3]

    return render(request, "main/home.html", {
        "teams": teams,
        "games": games,
    })
