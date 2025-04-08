from django import forms
from .models import Team
from games.models import Game

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"

class AddTournamentForm(forms.Form):

    tournament_name = forms.CharField(label="Add New Tournament", required=False)


class AddGamesToTeam(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['games']
        widgets = {
            'games': forms.CheckboxSelectMultiple()
        }