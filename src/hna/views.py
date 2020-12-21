from django.contrib.auth import authenticate, login, logout, get_user_model

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm

def homepage(request):
	context = {}
	return render(request, 'home_page.html', context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'title': 'Log In',
        'form' : form
    }

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(request, username=username, password=password)

        print('username: ' + username )
        print('password: ' + password )

        if user is not None:
            print('User verified')
            print(username + ' logged in')
            login(request, user)

            return redirect('/')

        else:
            print('Error! User unknown')
            print('Authentication Failed!')

    return render(request, 'auth/login.html', context)


def logout_page(request):
	# if request.method == 'POST':
	logout(request)
	return redirect('home')


User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'title': 'Sign up',
        'form' : form
        }
    if form.is_valid():
        
        username  = form.cleaned_data.get('username')
        email     = form.cleaned_data.get('email')
        password  = form.cleaned_data.get('password')
        new_user  = User.objects.create_user(username, email, password)
        print(new_user)
        # return redirect('login')

    return render(request, 'auth/register.html', context)
