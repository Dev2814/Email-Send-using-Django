from django.contrib import admin
from django.urls import path
from SendingEmail import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup_user, name='signup_user'),
    path('login/', views.login_user, name = 'Login_user'),
    path("logout/", views.logout_user, name="logout_user"),
]
