from django.db import models
import django.utils.timezone

class Puser(models.Model):
	user_id=models.CharField(max_length=30,primary_key='true')
	user_name=models.CharField(max_length=30)
	email=models.CharField(max_length=30)
	phoneno=models.IntegerField();
	bdate=models.DateTimeField();
	password=models.CharField(max_length=20)
	
class Offers(models.Model):
	offer_id=models.CharField(max_length=30,primary_key='true')
	offer_details=models.TextField()
	
class Ticket(models.Model):
	ticket_id=models.CharField(max_length=30,primary_key='true')
	user_id=models.ForeignKey('Puser',on_delete='true')
	show_id=models.ForeignKey('Show',on_delete='true')

class Movie(models.Model):
	movie_id=models.CharField(max_length=30,primary_key='true')
	cinema_id=models.ForeignKey('Cinema',on_delete='true')
	movie_name=models.CharField(max_length=50)

class Cinema(models.Model):
	cinema_id=models.CharField(max_length=30,primary_key='true')
	cinema_name=models.CharField(max_length=50)
	email=models.CharField(max_length=30)
	phoneno=models.IntegerField();
	address=models.CharField(max_length=100)
	password=models.CharField(max_length=20)

	
class Show(models.Model):
	show_id=models.CharField(max_length=30,primary_key='true')
	cinema_id=models.ForeignKey('Cinema',on_delete='true')
	movie_id=models.ForeignKey('Movie',on_delete='true')
	time=models.DateTimeField()
	
class TicketOffer(models.Model):
	ticket_id=models.ForeignKey('Ticket',on_delete='true')
	offer_id=models.ForeignKey('Offers',on_delete='true')
