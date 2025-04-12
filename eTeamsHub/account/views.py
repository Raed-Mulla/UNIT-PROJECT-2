from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from .models import Profile
from .forms import AvatarForm
from teams.models import Team
# Create your views here.

def sign_in(request:HttpRequest):
    if request.user.is_authenticated:
        messages.success(request,"You are already Sign in","alert-success")
        return redirect("main:home")
    if request.method == "POST":

        user = authenticate(request,username=request.POST["username"],password=request.POST["password"])

        if user:
            login(request , user)
            messages.success(request,"logged in successfully","alert-success")
            return redirect("main:home")
        else:
            messages.error(request,"your email or password wrong")
    
    return render(request,"account/signin.html")

def sign_up(request:HttpRequest):
    if request.user.is_authenticated:
        messages.success(request,"You are already Sign in","alert-success")
        return redirect("main:home")
    if request.method == "POST":
        try:
            new_user = User.objects.create_user(username=request.POST["username"],password=request.POST["password"],email=request.POST["email"],first_name=request.POST["first_name"],last_name=request.POST["last_name"])
            new_user.save()

            
            avatar = request.FILES.get("avatar")
            Profile.objects.create(user=new_user, avatar=avatar)
            
            messages.success( request ,"Register Successfuly", "alert-success" )
            return redirect("account:sign_in")
        except Exception as e:
            messages.error(request , "Couldn't register user." , "alert-danger")
            print(e)

    return render(request,"account/signup.html")

def log_out(request:HttpRequest):
    logout(request)
    messages.success( request ,"log out Successfuly", "alert-success" )
    return redirect("main:home")


def profile_view(request:HttpRequest , user_name):

    if not request.user.is_authenticated:
        return redirect("account:sign_in")
    try:
        user = User.objects.get(username=user_name)
        profile = user.profile
    except Exception as e:
        return HttpResponse("error")
    
    return render(request, "account/profile.html")


def edit_avatar(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect("account:sign_in")
    profile = request.user.profile

    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Avatar updated successfully!" , "alert-success")
            return redirect("account:profile_view", user_name=request.user.username)
    else:
        form = AvatarForm(instance=profile)
    return render(request, "account/edit_avatar.html", {"form": form})

def favorite_team(request, team_id):
    if request.user.is_authenticated:
        try:
            team = Team.objects.get(id=team_id)
            request.user.profile.favorite_team.add(team)
            messages.success(request, "Favorite team updated!" , "alert-success")
        except Team.DoesNotExist:
            messages.error(request, "Team not found." , "alert-danger")
    return redirect("teams:team_detail", team_id=team_id)