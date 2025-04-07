from django.shortcuts import render , redirect
from django.http import HttpRequest,HttpResponse
from django.contrib import messages
from .forms import GameForm
from .models import Game


def add_game(request: HttpRequest):
    if request.method == "POST":
        form = GameForm(request.POST, request.FILES)
        game_name = request.POST.get("name", "").strip()

        if Game.objects.filter(name__iexact=game_name).exists():
            messages.warning(request, "the game is already exists", "alert-danger")
        else:
            if form.is_valid():
                form.save()
                messages.success(request, "Added game successfully" , "alert-success")
                return redirect("main:home")
            else:
                messages.error(request, "wrong added" , "alert-danger")
    else:
        form = GameForm()

    return render(request, "games/add_game.html", {"form": form})

def game_list(request):
    games = Game.objects.all()
    return render(request, "games/game_list.html", {"games": games})
