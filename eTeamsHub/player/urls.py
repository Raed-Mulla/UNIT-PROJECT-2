from django.urls import path
from . import views
app_name = "player"

urlpatterns = [
    path('add/<int:team_id>/', views.add_player, name='add_player'),
    path("team/<int:team_id>/", views.team_players, name="team_players"),
]