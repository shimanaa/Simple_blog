from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class loginForm(forms.Form):
	username = forms.CharField(max_length=50,widget=forms.TextInput
								(attrs={'class': 'form-control', 'placeholder': 'Your username or email'}))
	password = forms.CharField(max_length=50, widget=forms.PasswordInput
								(attrs={'class': 'form-control', 'placeholder': 'Your pass'}))


class registerForm(forms.Form):
	username = forms.CharField(max_length=50,widget=forms.TextInput
								(attrs={'class': 'form-control', 'placeholder': 'Your username'}))

	email = forms.EmailField(widget=forms.EmailInput
								(attrs={'class': 'form-control', 'placeholder': 'Your email'}))

	password1 = forms.CharField(label='password' , max_length=50, widget=forms.PasswordInput
								(attrs={'class': 'form-control', 'placeholder': 'Your pass'}))
								
	password2 = forms.CharField(label='confirm password' , max_length=50, widget=forms.PasswordInput
								(attrs={'class': 'form-control', 'placeholder': 'Your pass'}))

	def clean_username(self):
		data = self.cleaned_data['username']
		user = User.objects.filter(username=data)
		if user.exists():
			raise ValidationError('This Username already exists') 
		return data


	def clean_email(self):
		data = self.cleaned_data['email']
		user = User.objects.filter(email= data)
		if user.exists():
			raise ValidationError('This email already taken...')
		return data


	def clean(self):
		cleaned_data = super().clean()
		p1 = cleaned_data.get('password1')
		p2 = cleaned_data.get('password2')
		if p1 and p2:
			if p1 != p2:
				raise ValidationError('Your password not match :(')

		