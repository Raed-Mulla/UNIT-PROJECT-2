from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import PlayerForm
from .models import Player, Team

def add_player(request, team_id):
    if not request.user.is_staff:
        messages.error(request, "You are not allowed to access this page.", "alert-danger")
        return redirect("main:home")

    try:
        team = Team.objects.get(id=team_id)
    except Team.DoesNotExist:
        messages.error(request, "Team not found.", "alert-danger")
        return redirect("main:home")

    if request.method == "POST":
        form = PlayerForm(request.POST, request.FILES)
        player_name = request.POST.get("name", "").strip()

        if Player.objects.filter(name__iexact=player_name, team=team).exists():
            messages.warning(request, "This player already exists in the team.", "alert-danger")
        elif form.is_valid():
            player = form.save(commit=False)
            player.team = team
            player.save()
            messages.success(request, "Player added successfully!", "alert-success")
            return redirect("teams:team_detail", team_id=team.id)
        else:
            messages.error(request, "There was an error adding the player.", "alert-danger")
    else:
        form = PlayerForm()

    return render(request, "player/add_player.html", {"form": form, "team": team})

def team_players(request, team_id):
    team = Team.objects.filter(id=team_id).first()
    if not team:
        messages.error(request, "Team not found.", "alert-danger" )
        return redirect("main:home")

    players = team.players.all()
    return render(request, "player/team_players.html", {"team": team, "players": players})