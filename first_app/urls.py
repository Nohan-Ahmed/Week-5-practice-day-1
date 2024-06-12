from django.urls import path
from . import views
urlpatterns = [
    path('', views.profile, name='profile'),
    path('singup/', views.singup, name='singup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('change_pass/', views.change_pass, name='change_pass'),
]
