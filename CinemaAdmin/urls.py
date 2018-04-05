from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.home),
    path('profile/',views.profile),
    path('contact/',views.contact),
    path('about/',views.about),
    path('editPassword/',views.editPassword),
    path('editProfile/',views.editProfile),
    path('addNewMovie/',views.addNewMovie),
    path('add/',views.add),
    path('addNewOffer/',views.addNewOffer),
    path('add2/',views.add2),
    path('addNewShow/',views.addNewShow),
    path('add3/',views.add3)
    ]
