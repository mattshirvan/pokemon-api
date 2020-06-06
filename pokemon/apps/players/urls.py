from django.conf.urls import url
from .views import Players, logouts, register, logins

app_name = "players"

urlpatterns = [
    url(r'^$', Players.as_view(), name="players"),
    url(r'^register$', register, name="register"),
    url(r'^login$', logins, name="login"),
    url(r'^logout$', logouts, name="logout")
]