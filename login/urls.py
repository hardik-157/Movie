from django.urls import path
from . import views

urlpatterns = [
    path('', views.login1),
    path('logout/',views.logout),
    path('auth/', views.auth_view),
    path('loggedin/', views.loggedin),
    path('invalidlogin/', views.invalidlogin),
    path('signUp/', views.signUp),
    path('store/',views.store),
    path('cinstore/',views.cinstore),
    path('restore/',views.restore),
    path('recover/',views.recover),
    path('update/',views.update),
    path('updateProfile/',views.updateProfile),
    path('updatePassword/',views.update),
    path('updatePasswordCin/',views.updatePassword),
]
