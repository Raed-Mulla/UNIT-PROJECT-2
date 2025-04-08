from django.urls import path
from . import views

app_name = "teams"

urlpatterns = [
    path("add/" , views.add_team , name="add_team"),
    path("list/" , views.team_list,name="team_list"),
    path("<team_id>/", views.team_detail, name="team_detail"),
    path('<team_id>/add-tournament/', views.add_tournament, name='add_tournament'),
    path('<team_id>/add-games/', views.add_games_to_team, name='add_games'),
    path('<team_id>/remove-game/<game_id>/', views.remove_game_from_team, name='remove_game'),

]