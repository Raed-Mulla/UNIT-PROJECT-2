from django.urls import path
from . import views

app_name = "games"

urlpatterns = [
    path("add/" , views.add_game , name="add_game"),
    path("list/",views.game_list,name="game_list")
]