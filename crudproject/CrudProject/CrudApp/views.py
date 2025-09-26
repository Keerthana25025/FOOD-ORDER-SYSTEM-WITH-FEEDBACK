from django.shortcuts import render,redirect
from django.http import HttpResponse
from CrudApp.models import Student,Registers,Profile
from CrudApp.forms import Reg
from CrudApp.forms import RegistrationForm,ProfileForm
from django.contrib.auth import authenticate,login
from CrudProject import settings
from django.core.mail import send_mail

# Create your views here.
def create(request):
	if request.method=="POST":
		na=request.POST['uname']
		rnm=request.POST['rnm']
		age=request.POST['age']
		mb=request.POST['mbl']
		e=request.POST['em']
		add=request.POST['addr']
		Student.objects.create(name=na,rollnumber=rnm,age=age,mobile=mb,email=e,address=add)
		return redirect('/read')
	return render(request,'create.html',{})

def read(request):
	info=Student.objects.all()
	return render(request,'read.html',{'in':info})
def update(request,id):
	data=Student.objects.get(id=id)
	if request.method=="POST":
		data.name=request.POST['uname']
		data.rollnumber=request.POST['rnm']
		data.age=request.POST['age']
		data.mobile=request.POST['mbl']
		data.email=request.POST['em']
		data.address=request.POST['addr']
		data.save()
		return redirect('/read')
	return render(request,'update.html',{'data':data})

def delete(request,id):
	ob=Student.objects.get(id=id)
	if request.method=="POST":
		ob.delete()
		return redirect('/read')
	return render(request,'delete.html',{'info':ob})

def reg(request):
	if request.method=="POST":
		form=Reg(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/display')
	form=Reg()
	return render(request,'reg.html',{'info':form})
def display(request):
	data=Registers.objects.all()
	return render(request,'display.html',{'info':data})

def up(request,id):
	a=Registers.objects.get(id=id)
	if request.method=="POST":
		u=Reg(request.POST,instance=a)
		if u.is_valid():
			u.save()
			return HttpResponse("<h2>Data is Updates Successfully</h2>")
			return redirect('/display')
	u=Reg(instance=a)
	return render(request,'up.html',{'u':u})

def de(request,id):
	d=Registers.objects.get(id=id)
	if request.method=="POST":
		d.delete()
		return redirect('/display')
	return render(request,'del.html',{'d':d})

def register(request):
	form=RegistrationForm()
	if request.method=="POST":
		form=RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("<h2>Details Are Submitted!!!</h2>")
	return render(request,'register.html',{'form':form})

def signin(request):
	if request.method=="POST":
		username=request.POST['uname']
		password=request.POST['pswd']
		u=authenticate(username=username,password=password)
		if u:
			login(request,u)
			return HttpResponse("<h2>Authenticated User</h2>")
		else:
			return HttpResponse("<h2>Invalid Credentials</h2>")
	return render(request,'signin.html',{})

def profile(request):
	form=ProfileForm()
	if request.method=="POST":
		form=ProfileForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponse("<h2>Image is Uploaded Successfully!!!</h2>")

	return render(request,'profile.html',{'f':form})

def data(request):
	d=Profile.objects.all()
	return render(request,'data.html',{'data':d})

def mail(request):
	if request.method=="POST":
		rcr=request.POST['sn']
		sbj=request.POST['sb']
		m=request.POST['msg']
		t=settings.EMAIL_HOST_USER
		res=send_mail(sbj,m,t,[rcr])
		if res==1:
			print("Mail Sent")
		else:
			print("Not Sent")
	return render(request,'mail.html',{})

def home(request):
	return render(request,'home.html',{})