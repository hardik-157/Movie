from django.shortcuts import render_to_response,redirect,render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.http import JsonResponse
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from login.models import *
from django.contrib.auth import *
from login.forms import *

@login_required(login_url = '/login/')

def seats(request): #to show the seat arrengments...
		c={}
		c.update(csrf(request))
		sid = request.POST.get('sid','')
		fid = request.POST.get('fid')
		movie_name = request.POST.get('movie_name')
		request.session['sid'] = sid
		request.session['fid'] = fid
		show = Show.objects.filter(show_id = int(sid))
		seat = show[0].seat
		time = show[0].time
		print(request.session['cinema_id'])
        #seat="0110100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"
		com='1'
		c['chart']=seat
		c['com']=com
		c['movie_name'] = movie_name
		c['time'] = time
		price1=show[0].price_ex;
		price2=show[0].price_pr;
		c['price1']=price1
		c['price2']=price2
		return render(request,'seats.html',c)

@login_required(login_url = '/login/')

def bookings(request): #to show all the bookings done by user...
        c = {}
        c.update(csrf(request))
        user = User.objects.get(id = request.user.id)
        ticket = Ticket.objects.filter(user_id = user.username)
        c['ticket'] = ticket
        return render(request,'bookings.html',c)

@login_required(login_url = '/login/')

def book(request): #to store the booking data in to database...
	c={}
	c.update(csrf(request))
	sid = request.session['sid']
	fid = request.session['fid']
	show = Show.objects.get(show_id = sid)
	show.seat = request.POST.get('chart')
	show.save()
	offer = None
	if fid is not None:
		offer = Offers.objects.get(offer_id = int(fid))
	if offer is None:
		cin= Cinema.objects.get(cinema_id=request.session['cinema_id'])
		offer = Offers.objects.get(cinema_id=cin , offer_name="default")
	price = request.POST.get('total')
	count = request.POST.get('count')
	user = request.user.username
	puser = Puser.objects.filter(user_id = user)
	ticket = Ticket(user_id = puser[0], show_id = show, seat = int(count), price = int(price), offer_id = offer)
	ticket.save()
	request.session['ticket_id'] = ticket.ticket_id
	return HttpResponseRedirect('/book/ticket/')
@login_required(login_url = '/login/')
def ticket(request): #to display the ticket details after successfull booking...
        c = {}
        c.update(csrf(request))
        ticket_id = request.session['ticket_id']
        ticket = Ticket.objects.get(ticket_id = int(ticket_id))
        c['ticket_id'] = ticket.ticket_id
        c['seat'] = ticket.seat
        c['price'] = ticket.price
        #show = Show.objects.get(show_id = ticket.show_id)
        show = ticket.show_id
        c['show_time'] = show.time
        #movie = Movie.objects.get(movie_id = show.movie_id)
        movie = show.movie_id
        c['movie_name'] = movie.movie_name
        #cinema = Cinema.objects.get(cinema_id = show.cinema_id)
        cinema = show.cinema_id
        c['cinema_name'] = cinema.cinema_name
        return render(request,'ticket.html',c)
	
