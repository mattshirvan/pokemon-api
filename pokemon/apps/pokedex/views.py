from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Index(LoginRequiredMixin, View):
    login_url = "/"
    redirect_field_name = 'players'

    def get(self, request):
        return render(request, "pokedex/index.html")
    def post(self, request):
        return render(request, "pokedex/index.html")

