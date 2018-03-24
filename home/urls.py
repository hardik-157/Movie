from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('contact/',views.contact),
    path('profile/',views.profile),
    path('movieandevents/',views.movieandevent),
    path('editProfile/',views.editProfile),
    path('editPassword/',views.editPassword),
    ]
