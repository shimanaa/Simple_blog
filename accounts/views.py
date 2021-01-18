from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import loginForm, registerForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


def user_login(request):
	if request.method == 'POST':
		form = loginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(request, username=username, password= password)
			if user is not None:
				login(request, user)
				messages.success(request, 'Your Logged in Successfully :)', 'success')
				return redirect('blog:allArticle')
			else:
				messages.warning(request, 'Wrong username or password :(', 'danger')
	else:
		form = loginForm()
	return render(request, 'accounts/login.html', {'form': form})


def user_register(request):
	if request.method == 'POST':
		form = registerForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			User.objects.create_user(cd['username'], cd['email'], cd['password1'])
			messages.success(request, 'Your registered, Now log in', 'success')
			return redirect('accounts:user_login')
	else:
		form = registerForm()
	
	return render(request, 'accounts/register.html', {'form': form})


def user_logout(request):
	logout(request)
	messages.success(request, 'Your logged successfully', 'success')
	return redirect('blog:allArticle')

