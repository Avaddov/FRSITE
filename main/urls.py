from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('merch', views.merch, name='merch'),
    path('gallery', views.gallery, name='gallery'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('submit', views.submitmedia, name='submit'),
    path('gamereviews', views.gamereviews, name='gamereviews'),
    path('gamereview/<int:id>', views.gamereview, name='gamereview'),
    path('search_twitch', views.searchgame, name='search_twitch'),
    path('create_review/<int:twitch_id>', views.create_review, name='create_review')

]

#