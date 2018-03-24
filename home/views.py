from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from login.models import *
from django.contrib.auth import *
from django.contrib.auth.models import User

def home(request):
    c={}
    c.update(csrf(request))
    if request.user.is_authenticated:
        return render(request,'home.html',c)
    else:
        return HttpResponseRedirect('/login/invalidlogin')
def about(request):
    c={}
    c.update(csrf(request))
    if request.user.is_authenticated:
        return render(request,'about.html',c)
    else:
        return HttpResponseRedirect('/login/invalidlogin')
def contact(request):
    c={}
    c.update(csrf(request))
    if request.user.is_authenticated:
        return render(request,'contact.html',c)
    else:
        return HttpResponseRedirect('/login/invalidlogin')
def profile(request):
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
def editPassword(request):
    c = {}
    c.update(csrf(request))
    return render(request,'update_password.html',c)
    
def editProfile(request):
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
def movieandevent(request):
    c={}
    c.update(csrf(request))
    if request.user.is_authenticated:
        return render(request,'movies_events.html',c)
    else:
        return HttpResponseRedirect('/login/invalidlogin')
# Create your views here.
