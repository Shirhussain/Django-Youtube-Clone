from django.urls import path
from .views import (
    IndexView, TrendingListView,VideoDetailView,
    channels,
    category,
    channel, login, register, reset, search,
    history,settings,wishlist,myChannels,playLists
)


urlpatterns = [
    path('', IndexView.as_view(), name = "index"),
    path('trending/', TrendingListView.as_view(), name="trending"),
    path('channels/', channels, name="channels"),
    path('channel/<int:pk>/', channel, name="channel"),
    path('video/<int:pk>/',VideoDetailView.as_view(), name="video"),
    path('category/', category, name="category"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('reset/', reset, name="reset"),
    path('search/', search, name="search"),
    path('history/', history, name="history"),
    path('settings/', settings, name="settings"),
    path('wishlist/', wishlist, name="wishlist"),
    path('mychannels/', myChannels, name="mychannels"),
    path('playlists/',playLists, name="playlists"),
]
