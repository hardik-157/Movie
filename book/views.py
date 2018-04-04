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

def seats(request):
	c={}
	c.update(csrf(request))
	seat="0110100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"
	com='1'
	c['chart']=seat
	c['com']=com
	price1=10;
	price2=20;
	c['price1']=price1
	c['price2']=price2
	return render(request,'seats.html',c)
	
def ticket(request):
	c={}
	c.update(csrf(request))
	print(request.POST.get('chart'))
	return render(request,'seats.html',c)
	