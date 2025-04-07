from django.urls import path
from . import views

app_name = "teams"

urlpatterns = [
    path("add/" , views.add_team , name="add_team"),
    path("list/" , views.team_list,name="team_list"),
    path("<team_id>/", views.team_detail, name="team_detail"),
]