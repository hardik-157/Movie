from django.shortcuts import render_to_response,redirect,render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from login.models import *
from django.contrib.auth import *
from login.forms import *
from django.contrib.auth.forms import PasswordChangeForm

def login1(request):
	c ={}
	c.update(csrf(request))
	return render(request,'index.html',c)
def restore(request):
        c={}
        c.update(csrf(request))
        return render(request,'restore.html',c)
def updateProfile(request):
        c = {}
        c.update(csrf(request))
        name= request.POST.get('name','')
        phone= request.POST.get('phone', '')
        date= request.POST.get('date', '')
        if request.user.is_authenticated:
                id = request.user.id
                user = User.objects.get(id = id)
                if user is not None:
                        username = user.username
                        list2 = Puser.objects.filter(user_id = username)
                        count = list2.count()
                        if int(count)>0:
                                pUser = list2[0]
                                pUser.user_name = name
                                pUser.phoneno = phone
                                pUser.bdate = date
                                pUser.save()
                        else:
                                return render(request,'edit_profile.html',c)
                return HttpResponseRedirect('/home/profile')
        else:
                return HttpResponseRedirect('/login/invalidlogin')
def update(request):
	c={}
	c.update(csrf(request))
	id = request.user.id
	puser = User.objects.get(id=id)
	form = PasswordChangeForm(request.user, request.POST)
	c['form']=form
	if form.is_valid():
		profile= Puser.objects.get(user_id=puser.username);
		profile.password=request.POST.get('new_password1','');
		profile.save()
		user = form.save()
		update_session_auth_hash(request, user)  # Important!
		#messages.success(request, 'Your password was successfully updated!')
	else:
                return render(request,'home.html',c)
		#return render(request,'home.hmtl',c)
	return render(request,'home.html',c)
def recover(request):
        c={}
        c.update(csrf(request))
        username = request.POST.get('username')
        bdate = request.POST.get('date')
        l = [bdate]
        list = Puser.objects.filter(user_id = username)
        password = ' '
        if int(list.count())>0:
                date = [list[0].bdate];
                d1 = str(l[0])
                d2 = str(date[0])
                cmp = d2.find(d1)
                if int(cmp>=0):
                        password = 'Your password is:'+str(list[0].password)
                else:
                        password = password+'Invalid details!'
        else:
                password = password+'Invalid details!'
        c['msg'] = password
        return render(request,'restore.html',c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/login/loggedin/')
	else:
		return HttpResponseRedirect('/login/invalidlogin/')

@login_required(login_url = '/login/')

def loggedin(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/home/')
	else:
		return HttpResponseRedirect('/login/invalidlogin/')

def invalidlogin(request):
	c ={}
	c.update(csrf(request))
	c['q']="Invalid UserName or PassWord"
	return render(request,'index.html',c)
	
def signUp(request):
	c ={}
	c.update(csrf(request))
	c['role']="member"
	return render(request,'signup.html',c)

def store(request):
	username= request.POST.get('username', '')
	name= request.POST.get('name','')
	password1= request.POST.get('password1', '')
	password2= request.POST.get('password2', '')
	email= request.POST.get('email','')
	phone= request.POST.get('phone', '')
	date= request.POST.get('date', '')
	c ={}
	c.update(csrf(request))
	form = SignUpForm(request.POST)
	c['form']=form;
	c['role']="member"
	if form.is_valid():
			profile= Puser(user_id=username,user_name=name,email=email,phoneno=phone,bdate=date,password=password1)
			profile.save()
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return render(request,'home.html')
	return render(request,'signup.html',c)

def cinstore(request):
	username= request.POST.get('username', '')
	name= request.POST.get('name','')
	password1= request.POST.get('password1', '')
	password2= request.POST.get('password2', '')
	email= request.POST.get('email','')
	phone= request.POST.get('phone', '')
	address= request.POST.get('address','')
	c={}
	c.update(csrf(request))
	form = SignUpForm(request.POST)
	c['form']=form;
	c['role']="manager"
	if form.is_valid():
			profile= Cinema(cinema_id=username,cinema_name=name,email=email,phoneno=phone,password=password1,address=address)
			profile.save()
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return render(request,'home.html')
	return render(request,'signup.html',c)
	
def logout(request):
	auth.logout(request)
	return render(request,'index.html')
