
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('targeting/', views.targeting, name="targeting"),
    path('engagement/', views.engagement, name="engagement"),
    path('instaConn/', views.instaConn, name="instaConn"),
    path('myprofile/', views.myprofile, name="myprofile"),

]
