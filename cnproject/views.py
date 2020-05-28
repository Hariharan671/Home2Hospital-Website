from django.shortcuts import render
#from cnproject.forms import NewUserForm,NewUser,Facilities,Details
import sys

from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from cnproject.models import UserProfileInfo,h2h

def tracker(request):
	return render(request,'index.html')
def donate(request):
	return render(request,'donate.html')

def home(request):
	return render(request,'Home.html')

def information(request):
	return render(request,'information.html')

def register(request):

	registered = False

	if(request.method=='POST'):
		registered=True
		a=request.POST.get('name')
		b=request.POST.get('dob')
		c=request.POST.get('location')
		d=request.POST.get('phone')
		e=request.POST.get('secret')
		model = UserProfileInfo(first_name=a,dob=b,location=c,phone=d,secret=e)
		model.save()
	return render(request,'login.html',{'registered':registered})


class A:
	def __init__(self):
		self.logged=False
		self.c=None

	def index(self,request):
		self.logged=False
		return render(request,'login.html')

	def login(self,request):
		if(self.logged==True):
			return render(request,'information.html',{'current':self.c})
		else:
			if request.method=='POST':
				a=request.POST.get('phone')
				b=request.POST.get('secret')
				#d = UserProfileInfo(phone=a,secret=b)
				self.c = UserProfileInfo.objects.filter(phone=a,secret=b).first()
				if(self.c==None):
					return render(request,'loginerror.html')
				else:
					self.logged=True
					return render(request,'information.html',{'current':self.c})
			else:
				self.logged=False
				return render(request,'login.html')

	def facilities(self,request):
		if(self.logged):
			facilities=False
			if request.method=='POST':
				facilities=True
				a=request.POST.get('radio3')
				b=request.POST.get('radio4')
				e=request.POST.get('radio5')
				d=request.POST.get('radio1')
				#Update
				self.c.mask= a=='on'
				self.c.hand_sanitizer= b=='on'
				self.c.proper_ventilation= e=='on'
				self.c.wheel_chair= d=='on'
				self.c.save()
				return render(request,'information.html',{'facility':facilities,'current':self.c})
			else:
				return render(request,'information.html',{'facility':facilities,'current':self.c})
		else:
			return render(request,'login.html')

	def staff(self,request):
		if(self.logged):
			staff=False
			if request.method=='POST':
				staff=True
				a=request.POST.get('radio6')
				b=request.POST.get('radio2')
				d=request.POST.get('bodytemp')
				e=request.POST.get('pulse')
				f=request.POST.get('bp')
				#Update
				self.c.body_temperature= d
				self.c.blood_pressure= f
				self.c.pulse= e
				self.c.cleaning= a=='on'
				self.c.facilities= b=='on'
				self.c.save()
				return render(request,'information.html',{'staff':staff,'current':self.c})
			else:
				return render(request,'information.html',{'staff':staff,'current':self.c})
		else:
			return render(request,'login.html')
	def logout(self,request):
		self.c=None
		self.logged=False
		return render(request,'login.html')

def doubt(request):
	if(request.method=="POST"):
		b=request.POST.get("name")
		c=request.POST.get("age")
		d=request.POST.get("sex")
		e=request.POST.get("country")
		f=request.POST.get("state")
		g=request.POST.get("phone")
		h=request.POST.get("email")
		j=request.POST.get("question")
		m = h2h(name=b,dob=c,sex=d,country=e,state=f,phone=g,email=h,problem=j)
		m.save()
		return render(request,'xray.html',{'a':False})
	else:
		return render(request,'xray.html',{'a':True});

def lead(request):
	return render(request,'xray.html',{'a':True});




