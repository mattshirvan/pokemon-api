"""pokemon URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^pokedex', include("apps.pokedex.urls", namespace="pokedex")),
    url(r'^', include("apps.players.urls", namespace="players"))
]
