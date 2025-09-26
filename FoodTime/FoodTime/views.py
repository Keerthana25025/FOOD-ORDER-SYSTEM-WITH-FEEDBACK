from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import FoodItem,Registers,Feedback,Order
from django.contrib.auth import authenticate,login
from FoodProject import settings
# Create your views here.


def index(request):
	return render(request,'index.html')

def home(request):
	return render(request,'home.html')

def food(request):
    items = FoodItem.objects.all()
    return render(request, 'food.html', {'items': items})

def order(request,no):
    try:
        item = FoodItem.objects.get(id=no)
    except FoodItem.DoesNotExist:
        raise Http404("Food item does not exist")
    
    if request.method == 'POST':
        add=request.POST.get('add')
        od = Order(item=item.id, add=add)
        od.save()
        return render(request, 'success.html', {'item': item})

    return render(request, 'order.html', {'item': item})

def delete(request):
	return render(request,'delete.html')

def register(request):
	if request.method=="POST":
		fna=request.POST['fname']
		lna=request.POST['lname']
		una=request.POST['uname']
		mb=request.POST['mbl']
		e=request.POST['em']
		Registers.objects.create(first_name=fna,last_name=lna,username=una,mobile=mb,email=e)
		return redirect('home')
	return render(request,'register.html',{})

def login(request):
	if request.method=="POST":
		username=request.POST['uname']
		password=request.POST['pswd']
		u=authenticate(username=username,password=password)
		if u:
			return HttpResponse("<h2>Authenticated User!</h2>")
			return redirect('admin')
		else:
			return HttpResponse("<h2>Invalid User !</h2>")
	return render(request,'login.html',{})

def feed(request):
	if request.method == 'POST':
		customer_name = request.POST.get('customer_name')
		email = request.POST.get('email')
		food_rating = request.POST.get('food_rating')
		delivery_rating = request.POST.get('delivery_rating')
		comments = request.POST.get('comments')
		Feedback.objects.create(
            customer_name=customer_name,
            email=email,
            food_rating=food_rating,
            delivery_rating=delivery_rating,
            comments=comments)
		return redirect('home')
	return render(request,'feed.html')

def review(request):
	info=Feedback.objects.all()
	return render(request,"review.html",{'re':info})