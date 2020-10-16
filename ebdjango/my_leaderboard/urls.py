from django.urls import path

from . import views
from my_leaderboard.views import HomePageView

urlpatterns = [
    # path('', views.index, name='index'),
    path('home', HomePageView.as_view(), name='home')
]
