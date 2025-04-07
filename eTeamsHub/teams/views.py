from django.shortcuts import render , redirect
from django.http import HttpRequest,HttpResponse
from django.contrib import messages
from .forms import TeamForm
from .models import Team

# Create your views here.
def add_team(request: HttpRequest):
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

    return render(request, "teams/team_detail.html", {"team": team})
