from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages

# Create your views here.

def register(request):
	if request.method == 'POST' :
		username = request.POST['username']
		pass1 = request.POST['pass1']
		pass2 = request.POST['pass2']

		if pass1 == pass2:
			if User.objects.filter(username=username).exists():
				messages.info(request,'Username taken')
				return redirect('register')
			else :
				user = User.objects.create_user(username = username, password = pass1)
				user.save();
				messages.info(request,'user created')
				return redirect('login')

		else :
			messages.info(request,'password not matching')
			return redirect('register')
		return redirect('home')
	else :
		return render(request,'jobseeker/register.html')



def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		pass1 = request.POST['pass1']

		user = auth.authenticate(username=username, password=pass1)

		if user is not None:
			auth.login(request,user)
			return redirect('home')
		else :
			messages.info(request,'Invalid Credentials')
			return redirect('login')

	else:
		return render(request,'jobseeker/login.html')