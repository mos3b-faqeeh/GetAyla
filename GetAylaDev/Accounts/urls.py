
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path('', views.register,name="register"),
path('login/', views.login,name="login"),
path('logout/', views.logout,name="logout"),
path('myprofile/', views.myprofile, name="myprofile"),
path('updatePass/', views.updatePass, name="updatePass"),

path('updatePayment/', views.updatePayment, name="updatePayment"),
path('updateNum/', views.updateNum, name="updateNum"),
path('updateEmail/', views.updateEmail, name="updateEmail"),

]
