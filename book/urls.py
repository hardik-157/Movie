from django.urls import path
from . import views

urlpatterns = [
	path('', views.seats),
	path('ticket/', views.ticket),
]