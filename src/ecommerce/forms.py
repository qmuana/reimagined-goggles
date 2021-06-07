from django import forms
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()
class ContactForm(forms.Form):
	fullname = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control', 
				'placeholder': 'Your full name'
				}
			)
		)
	email	 = forms.EmailField(
		widget=forms.EmailInput(
			attrs={
				'class':'form-control', 
				'placeholder':'Your email'
				}
			)
		)
	content  = forms.CharField(
		widget=forms.Textarea(
			attrs={
				'class': 'form-control',
				'placeholder': 'Your message'
				}
			)
		)

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if not 'gmail.com' in email:
			raise forms.ValidationError('Email has to be gmail!')
		return email




class LoginForm(forms.Form):
	username = forms.CharField(
		label=False,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'username or email address'
				}
			)
		)

	password = forms.CharField(
		label='No account?',
		widget=forms.PasswordInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'password'
				}
			)
		)

class RegisterForm(forms.Form):
	username  = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	email     = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	password  = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

	def clean_username(self):
		data = self.cleaned_data
		username = self.cleaned_data.get('username')
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError('username is taken')
		return username

	def clean_email(self):
		data = self.cleaned_data
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError('email is taken')
		return email

	def clean(self):
		data = self.cleaned_data
		password  = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password != password2:
			raise forms.ValidationError('Password must match!')
		return data
