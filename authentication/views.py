from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import User


def login_view(request):
	if request.user.is_authenticated:
		return redirect('/booking')
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(request, username=email, password=password)
		if user is not None:
			login(request, user)
			return redirect('/booking')
		else:

			return render(request, "login.html", {"success":"Failure to login!"})
	else:
		try:
			message = request.GET['success']
		except:
			message = ""
		return render(request, "login.html", {"success":message})
def logout_view(request):
	logout(request)
	return redirect('/login')


def register(request):
	if request.user.is_authenticated:
		return redirect('/login')

	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']	
		try:
			user = User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
			user.save()
			return redirect('/login?success=Successfully registered!')
		except Exception as e:
			print(e)
			return render(request, 'register.html', {"success":"Failure to register! Email already in database."})
	else:
		return render(request, 'register.html')


