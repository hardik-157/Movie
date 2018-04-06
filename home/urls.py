from django.urls import path
from . import views

urlpatterns = [
    path('location/',views.location),
    path('cinema/',views.cinema),
    path('', views.home),
    path('about/', views.about),
    path('contact/',views.contact),
    path('profile/',views.profile),
    path('editProfile/',views.editProfile),
    path('editPassword/',views.editPassword),
    path('movie/',views.movie),
    ]
