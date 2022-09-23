from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from accounts.forms import CreateUserForm

# Create your views here.
 
def registerUser(request):
	
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			
			mail = request.POST.get('email')
			subject = f'Welcome to Shortly'
			message = f'Hi {username}, Welcome to Shortly. Thank you for registering in our website.'
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [mail]
			send_mail(subject, message, email_from, recipient_list)

			messages.success(request, message=f'Welcome {username}, Your Account is created now')
			return redirect('login')
	else:
		form = CreateUserForm()
	context={'form':form}
	return render(request,'main/register.html',context=context)



def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('dashboard')
		else:
			messages.info(request, message='Username or Password is incorrect')
			return redirect('login')
	context = {}
	return render(request, 'main/login.html',context=context)


def logoutUser(request):
	logout(request)
	return redirect('index')

