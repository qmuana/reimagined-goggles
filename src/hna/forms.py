from django import forms
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()

class LoginForm(forms.Form):
	username = forms.CharField(
		label=False,
		widget=forms.TextInput(attrs={
				'class': 'user-input', 
				'placeholder': 'username or email'
				}
			)
		)

	password = forms.CharField(
		label=False,
		widget=forms.PasswordInput(attrs={
				'class': 'user-input', 
				'placeholder': 'password'
				}
			)
		)




class RegisterForm(forms.Form):
	username  = forms.CharField(
		label=False,
		widget=forms.TextInput(attrs={
				'class': 'user-input',
				'placeholder': 'username'
				}
			)
		)

	email     = forms.EmailField(
		label=False,
		widget=forms.EmailInput(attrs={
				'class': 'user-input',
				'placeholder': 'email'
				}
			)
		)

	password  = forms.CharField(
		label=False,
		widget=forms.PasswordInput(attrs={
				'class': 'user-input',
				'placeholder': 'password'
				}
			)
		)

	password2 = forms.CharField(
		label=False,
		widget=forms.PasswordInput(attrs={
				'class': 'user-input',
				'placeholder': 'confirm password'
				}
			)
		)

	
	def clean_username(self):
		data = self.cleaned_data
		username = data.get('username')
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError('username is taken')
		return username


	def clean_email(self):
		data  = self.cleaned_data
		email = data.get('email')
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError('email is taken')
		if not '@gmail.com' in email:
			raise forms.ValidationError('Email has to be gmail.')
		return email


	def clean(self):
		data = self.cleaned_data
		password  = data.get('password')
		password2 = data.get('password2')
		if password2 != password:
			raise forms.ValidationError('password must match.!!!')
		return data