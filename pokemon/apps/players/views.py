from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
class Players(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("pokedex:index")

        register = RegisterForm()
        logins = LoginForm()
        context = {'login': logins, 'register': register}
        return render(request, "players/player.html", context)
        

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        print(form)
    if form.is_valid():
        form.save()
    else:
        messages.error(request, "Invalid user credentials")
    return redirect(reverse("players:players"))


def logins(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password1']
        print(username)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            print("should be logged in")
            login(request, user)
            return redirect(reverse("pokedex:index"))
        else:
            messages.info(request, "Username or Password is incorrect")


def logouts(request):
    logout(request)
    return redirect(reverse("players:players"))