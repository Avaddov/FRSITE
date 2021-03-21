from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('merch', views.merch),
    path('gallery', views.gallery),
    path('userpage', views.userpage),

]