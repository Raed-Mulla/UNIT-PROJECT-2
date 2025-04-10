from django.shortcuts import render , redirect
from django.http import HttpRequest,HttpResponse
from django.contrib import messages
from .forms import TeamForm , AddTournamentForm , AddGamesToTeam
from .models import Team , Tournament
from games.models import Game

# Create your views here.
def add_team(request: HttpRequest):

    if not request.user.is_staff:
        messages.error(request, "You are not allowed to access this page." , "alert-danger")
        return redirect("main:home")
    
    if request.method == "POST":
        form = TeamForm(request.POST, request.FILES)
        team_name = request.POST.get("name", "").strip()

        if Team.objects.filter(name__iexact=team_name).exists():
            messages.warning(request, "This team already exists.", "alert-danger")
        elif form.is_valid():
            form.save()
            messages.success(request, "Team added successfully!", "alert-success")
            return redirect("main:home")
        else:
            messages.error(request, "There was an error adding the team." , "alert-danger")
    else:
        form = TeamForm()

    return render(request, "teams/add_teams.html", {"form": form})

def team_list(request):
    teams = Team.objects.all()
    return render(request, "teams/team_list.html", {"teams": teams})


def team_detail(request: HttpRequest, team_id):
    try:
        team = Team.objects.get(id=team_id)
    except Team.DoesNotExist:
        return render(request, "404.html", status=404)

    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = team in request.user.profile.favorite_team.all()
    players = team.players.all()

    return render(request, "teams/team_detail.html", {"team": team,"is_favorite": is_favorite , "players" : players})


def add_tournament(request, team_id):
    if not request.user.is_staff:
        messages.error(request, "You are not allowed to access this page." , "alert-danger")
        return redirect("main:home")
    try:
        team = Team.objects.get(id=team_id)


        if request.method == "POST":
            tournaments = AddTournamentForm(request.POST)

            if tournaments.is_valid():
                tournament_name = request.POST.get('tournament_name') 

                if tournament_name:
                    tournament, created = Tournament.objects.get_or_create(name=tournament_name)
                    team.tournaments.add(tournament)

                messages.success(request, "Tournament added successfully!" , "alert-success")
                return redirect("teams:team_detail", team_id=team.id)
            else:
                messages.error(request, "Something went wrong." , "alert-danger")
        else:
            tournaments = AddTournamentForm()
    except Team.DoesNotExist:
        return render(request, "404.html", status=404)

    return render(request, "teams/add_tournament.html", {"tournaments": tournaments, "team": team})


def add_games_to_team(request, team_id):
    if not request.user.is_staff:
        messages.error(request, "You are not allowed to access this page." , "alert-danger")
        return redirect("main:home")
    try:
        team = Team.objects.get(id=team_id)

        if request.method == "POST":
            game = AddGamesToTeam(request.POST, instance=team)
            if game.is_valid():
                game.save()
                messages.success(request, "Games added successfully!" , "alert-success")
                return redirect("teams:team_detail", team_id=team.id)
            else:
                messages.error(request, "Something went wrong.")
        else:
            game = AddGamesToTeam(instance=team)
    except Team.DoesNotExist:
        return render(request, "404.html", status=404)

    return render(request, "teams/add_games.html", {"game": game, "team": team})


def remove_game_from_team(request, team_id, game_id):
    if not request.user.is_staff:
        messages.error(request, "You are not allowed to access this page." , "alert-danger")
        return redirect("main:home")
    try:
        team = Team.objects.get(id=team_id)
        game = Game.objects.get(id=game_id)

        team.games.remove(game)
        messages.success(request, f"{game.name} removed from {team.name}" , "alert-success")
        return redirect("teams:team_detail", team_id=team.id)

    except Team.DoesNotExist:
        messages.error(request, "Team not found.")
        return render(request, "404.html", status=404)

    except Game.DoesNotExist:
        messages.error(request, "Game not found.")
        return render(request, "404.html", status=404)