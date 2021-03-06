"""bowling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from scoreboard import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^v1/bowling/players/(?P<player_id>[a-f0-9-]+)', views.players_api),
    url(r'^v1/bowling/players', views.players_api),
    url(r'^v1/bowling/games/(?P<game_id>[a-f0-9-]+)', views.games_api),
    url(r'^v1/bowling/games', views.games_api),
    url(r'^v1/bowling/scores/(?P<score_id>[a-f0-9-]+)', views.scores_api),
    url(r'^v1/bowling/scores', views.scores_api),
]
