from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path("signin/" , views.sign_in , name="sign_in"),
    path("signup/" , views.sign_up , name="sign_up"),
    path("logout/" , views.log_out , name="log_out"),
    path("profile/<user_name>",views.profile_view,name="profile_view"),
    path("profile/edit-avatar/", views.edit_avatar, name="edit_avatar"),
    path("set-favorite/<int:team_id>/", views.favorite_team, name="favorite_team"),
]