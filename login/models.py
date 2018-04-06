from django.db import models
import django.utils.timezone

class Puser(models.Model):
	user_id=models.CharField(max_length=30,primary_key='true')
	user_name=models.CharField(max_length=30)
	email=models.CharField(max_length=30)
	phoneno=models.CharField(max_length = 30);
	bdate=models.DateTimeField();
	password=models.CharField(max_length=20)

class City(models.Model):
        city=models.CharField(max_length=100)
class Offers(models.Model):
	offer_id=models.AutoField(primary_key='true')
	cinema_id=models.ForeignKey('Cinema',on_delete='true')
	offer_name=models.CharField(max_length=30)
	offer_details=models.TextField()
	
class Ticket(models.Model):
	ticket_id=models.AutoField(primary_key='true')
	seat = models.IntegerField()
	price = models.IntegerField()
	offer_id = models.ForeignKey('Offers',on_delete='true')
	user_id = models.ForeignKey('Puser',on_delete='true')
	show_id = models.ForeignKey('Show',on_delete='true')

class Movie(models.Model):
	movie_id=models.AutoField(primary_key='true')
	cinema_id=models.ForeignKey('Cinema',on_delete='true')
	movie_name=models.CharField(max_length=50)
	movie_details=models.TextField()
	rating=models.IntegerField()

class Cinema(models.Model):
	cinema_id=models.CharField(max_length=30,primary_key='true')
	cinema_name=models.CharField(max_length=50)
	email=models.CharField(max_length=30)
	phoneno=models.CharField(max_length=30)
	city=models.CharField(max_length=100)
	address=models.CharField(max_length=100)
	password=models.CharField(max_length=20)

	
class Show(models.Model):
	show_id=models.AutoField(primary_key='true')
	cinema_id=models.ForeignKey('Cinema',on_delete='true')
	movie_id=models.ForeignKey('Movie',on_delete='true')
	time=models.CharField(max_length=100)
	seat=models.CharField(max_length=100)
	price_ex=models.IntegerField()
	price_pr=models.IntegerField()
	
class TicketOffer(models.Model):
	ticket_id=models.ForeignKey('Ticket',on_delete='true')
	offer_id=models.ForeignKey('Offers',on_delete='true')
