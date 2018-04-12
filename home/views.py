from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from login.models import *
from django.contrib.auth import *
from django.contrib.auth.models import User
@login_required(login_url = '/login/')
def location(request): #view for getting users location...
    c = {}
    c.update(csrf(request))
    cty = {}
    city_ob = City.objects.all()
    for ci in city_ob:
        cin_list = Cinema.objects.filter(city = ci.city)
        cty[str(ci.city)] = cin_list
    c['city'] = cty
    c['test'] = city_ob
    return render(request,'location.html',c)

@login_required(login_url = '/login/')

def cinema(request): #view for changing the location...
	c = {}
	c.update(csrf(request))
	cty = {}
	city_ob = City.objects.all()
	for ci in city_ob:
		cin_list = Cinema.objects.filter(city = ci.city)
		request.session['cin_id']=cin_list[0].cinema_id;
		print(request.session['cin_id'])
		cty[str(ci.city)] = cin_list
	c['city'] = cty
	c['test'] = city_ob
	return render(request,'cinema.html',c)

@login_required(login_url = '/login/')

def home(request): #home page view for user...
	c={}
	movies = {}
	cid = request.GET.get('cid','')
	if (cid!=''):
		request.session['cinema_id'] = cid
	else:
		return HttpResponseRedirect('/home/location/')
	cin_id = request.session['cinema_id']
	mov = Movie.objects.filter(cinema_id = cin_id)
	for	i in mov:
		l = [i.movie_name,i.movie_details]
		movies[i.movie_id] = l
	c['movies'] = movies
	offers = {}
	off = Offers.objects.filter(cinema_id = cin_id)
	for j in off:
		if j.offer_name!="default":
			offers[j.offer_name] = j.offer_details
	c['offers'] = offers
	c.update(csrf(request))
	if request.user.is_authenticated:
		return render(request,'home.html',c)
	else:
		return HttpResponseRedirect('/login/invalidlogin')

@login_required(login_url = '/login/')

def about(request): #view for about page...
    c={}
    c.update(csrf(request))
    if request.user.is_authenticated:
        return render(request,'about.html',c)
    else:
        return HttpResponseRedirect('/login/invalidlogin')

@login_required(login_url = '/login/')

def contact(request): #view for contact page
    c={}
    c.update(csrf(request))
    if request.user.is_authenticated:
        return render(request,'contact.html',c)
    else:
        return HttpResponseRedirect('/login/invalidlogin')

@login_required(login_url = '/login/')

def profile(request): #view to display user profile...
    c={}
    c.update(csrf(request))
    if request.user.is_authenticated:
        id = request.user.id
        user = User.objects.get(id = id)
        if user is not None:
            username = user.username
            list2 = Puser.objects.filter(user_id = username)
            count = list2.count()
            if int(count)>0:
                user_name = list2[0].user_id
                full_name = list2[0].user_name
                email = list2[0].email
                phoneno = list2[0].phoneno
                bdate = list2[0].bdate
                c['user_name'] = user_name
                c['full_name'] = full_name
                c['email'] = email
                c['phoneno'] = phoneno
                c['bdate'] = bdate
            c['count'] = username
        return render(request,'profile1.html',c)
    else:
        return HttpResponseRedirect('/login/invalidlogin')

@login_required(login_url = '/login/')

def editPassword(request): #view for password edit page...
    c = {}
    c.update(csrf(request))
    return render(request,'update_password.html',c)
    
@login_required(login_url = '/login/')

def editProfile(request): #view for profile edit page...
    c={}
    c.update(csrf(request))
    if request.user.is_authenticated:
        id = request.user.id
        user = User.objects.get(id = id)
        c['error'] = ' '
        if user is not None:
            username = user.username
            list2 = Puser.objects.filter(user_id = username)
            count = list2.count()
            if int(count)>0:
                full_name = list2[0].user_name
                email = list2[0].email
                phoneno = list2[0].phoneno
                bdate = list2[0].bdate
                c['full_name'] = full_name
                c['email'] = email
                c['phoneno'] = phoneno
                c['bdate'] = bdate
            else:
                c['error'] = 'Something is goping wrong!'
        else:
            c['error'] = 'Something is going wrong!'
        return render(request,'edit_profile.html',c)
    else:
        return HttpResponseRedirect('/login/invalidlogin')

@login_required(login_url = '/login/')

def movie(request): #view for showing showa and movie details...
	c = {}
	c.update(csrf(request))
	key = request.GET.get('key','')
	if key=="":
		return HttpResponseRedirect('/home/location/')
	if 'cinema_id' not in request.session:
		return HttpResponseRedirect('/home/location/')
	request.session['movie_id'] =  int(key)
	movie = Movie.objects.filter(movie_id = int(key))
	cid = request.session['cinema_id']
	offer = Offers.objects.filter(cinema_id = cid)
	show = Show.objects.filter(cinema_id = cid,movie_id = int(key))
	c['offer'] = offer
	c['show'] = show
	c['movie_name'] = movie[0].movie_name
	c['movie_details'] = movie[0].movie_details
	c['default']="default"
	return render(request,'movie.html',c)
