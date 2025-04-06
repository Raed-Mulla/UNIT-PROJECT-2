from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from .models import Profile
# Create your views here.

def sign_in(request:HttpRequest):
    
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

    if request.method == "POST":
        try:
            new_user = User.objects.create_user(username=request.POST["username"],password=request.POST["password"],email=request.POST["email"],first_name=request.POST["first_name"],last_name=request.POST["last_name"])
            new_user.save()

            Profile.objects.create(user=new_user)
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

    try:
        user = User.objects.get(username=user_name)
        profile = user.profile
    except Exception as e:
        return HttpResponse("error")
    
    return render(request, "account/profile.html")
